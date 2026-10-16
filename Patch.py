"""
===============================================================================
CAS (Cache Audio Shenanigans) - Patch.py-chan Tool.
Authored originally by TesterLan (TL) otherwise known as LanVTester In Github.
===============================================================================
"""

import glob
import os
import random
import re
import shutil
import sys
import traceback

# =============================================================================
# CRASH GUARD: Keeps CMD window open if ANY unhandled exception occurs... smh..
# =============================================================================

def patch_crash_guard(exc_type, exc_value, exc_tb):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_tb)
        return
    traceback.print_exception(exc_type, exc_value, exc_tb)
    print("\n" + "=" * 65)
    print("[!] OH NO! Please check the traceback above and send the Issue over to LanVTester CAS Issues Github.")
    print("=" * 65)
    input("[?] Press Enter to exit...")

sys.excepthook = patch_crash_guard


# Ensure the working directory is always where patch.py lives
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# =================================================================================================================================

def print_banner() -> None:
    """Displays a clean startup banner."""
    print("=" * 65)
    print(" CAS (Cache Audio Shenanigans) - PATCH.PY-CHAN TOOL")
    print(" Authored by TesterLan (TL) | LanVTester")
    print("=" * 65 + "\n")


def find_audio_file() -> str:
    """
    Finds the audio cache file dynamically even if it has a custom name!
    Supports CLI arguments / Drag-and-Drop, wildcards, and interactive selection.
    
    TL: WE'RE I HUMAN, I THINK.. I WOULD DIE OF IT.. BUT I AM NOT..
    """
    # 0. Did the user drag and drop something?
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg.endswith(".bak"):
            print("-" * 65)
            print("TL: ...seriously? you just dragged a .bak file onto patch.py???")
            print("TL: You're looking for restore.py, NOT patch.py, you absolute idiot of tomfoolery!")
            print("TL: What type of PERSON drags a .bak file onto a patch.py???")
            print("-" * 65 + "\n")
            input("Press Enter to exit...")
            sys.exit()
        if arg.endswith(".txt") and os.path.exists(sys.argv[1]):
            return sys.argv[1]

    # 1. Search patterns in order of specificity
    all_txt = [f for f in glob.glob("*.txt") if not f.lower().endswith(".bak")]

    cache_candidates = [
        f for f in all_txt 
        if "cache-audio" in f.lower() or "cacheaudio" in f.lower()
    ]
    audio_candidates = [
        f for f in all_txt 
        if "audio" in f.lower()
    ]

    candidates = sorted(set(cache_candidates or audio_candidates))

    # 2. Handle what we find, no its I. I DID THIS ALL MHUAHAHAHAHAHAAHA -TL
    if not candidates:
        print("-" * 65)
        print("[!] Main Error : Could not find any audio text files in this folder!")
        print("[!] Also Error : It needs to be in the DoL folder where audio/ and img/ exist!")
        print("[*] Extra Hint : Make sure both CacheAudio.txt and patch.py are present!")
        print("-" * 65 + "\n")
        manual_name = input("Enter your custom text file name manually (or press Enter to exit): ").strip()
        
        if manual_name.lower().endswith(".bak"):
            print("\n" + "-" * 65)
            print("TL: A .bak file is NOT music! You cannot inject a backup into your BGM!")
            print("TL: Nice try trying to create an HTML Inception monster.")
            print("TL: Who the hell tries that anyway? OH! ITS YOU!!!")
            print("\nTL: ITS YOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("-" * 65 + "\n")
            input("Press Enter to exit...")
            sys.exit()

        if manual_name and os.path.exists(manual_name):
            return manual_name

        print("\n" + "-" * 65)
        print("[*] Very Specific Error: If this keeps happening while you did everything right,")
        print("    give patch.py a moment to load in the folder, or close Explorer and retry.")
        print("-" * 65 + "\n")
        input("Press Enter to exit...")
        sys.exit()

    if len(candidates) == 1:
        return candidates[0]

    # Multiple audio packs found
    print("-" * 65)
    print(" MULTIPLE AUDIO PACKS DETECTED")
    print("-" * 65)
    print("Pick which audio pack you want to patch:\n")
    for idx, name in enumerate(candidates, 1):
        print(f"  [{idx}] {name}")
    print("-" * 65)
    
    choice = input(f"Choose a file (1-{len(candidates)}) [Default 1]: ").strip()
    print()
    if choice.isdigit() and 1 <= int(choice) <= len(candidates):
        return candidates[int(choice) - 1]
    return candidates[0]


def find_html_file() -> str:
    """Finds the DoL HTML file intelligently and not blind, even tho it is."""
    patterns = ["*DoL*.html", "*Degrees*Lewdity*.html", "*.html"]
    for pattern in patterns:
        found = [f for f in glob.glob(pattern) if not f.endswith((".bak", ".tmp"))]
        if found:
            return max(found, key=lambda filepath: os.path.getmtime(filepath))

    print("-" * 65)
    print("[!] Main Error: No DoL HTML file found in this folder!")
    if glob.glob("*.bak"):
        print("\n[*] TesterLan's Life Saver: WAIT! I see a .bak file right there!")
        print("TL: Did you delete or rename your game? Run restore.py to bring it back first!")
    else:
        print("[!] Also Error: It needs to be in the DoL folder where your main game exists!")
        print("[*] Cheesy Hint: Did you run this while patch.py was still in the CAS folder?")
    print("-" * 65 + "\n")
    input("Press Enter to exit...")
    sys.exit()


# =============================================================================
# DYNAMIC TRACK PARSER & SMART SEPARATION | OWAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# =============================================================================

CACHE_REGEX = re.compile(
    r'''<<cacheaudio\s+["'](?P<id>[^"']+)["']\s+["'](?P<path>[^"']+)["']\s*>>''',
    re.IGNORECASE,
)

POCKET_REGEX = re.compile(
    r"(setup\.pocketMusicTracks\s*=\s*\[)([\s\S]*?)(\]\s*;)",
    re.MULTILINE,
)


def extract_vanilla_manifest(html_content: str, backup_file: str) -> set[str]:
    """
    Headphones List 1.
    Extracts the official vanilla track paths directly from the game's HTML or .bak.
    This guarantees 120% of potential accuracy without hardcoding track names!!!! I think... tch.
    Simply scans the clean game to make a checklist of vanilla music.
    """
    source = html_content
    if os.path.exists(backup_file):
        try:
            with open(backup_file, "r", encoding="utf-8") as bf:
                source = bf.read()
        except OSError:
            pass

    match = POCKET_REGEX.search(source)
    if not match:
        return set()

    # Extract all string literals inside the array
    tracks = re.findall(r'''["']([^"']+)["']''', match.group(2))
    return {
        t.replace("\\", "/").strip().lower()
        for t in tracks
        if not t.strip().startswith("//") and not t.strip().startswith("/*")
    }


def is_vanilla_track(path: str, vanilla_manifest: set[str]) -> bool:
    """
    Headphones List 2.
    Dynamically determines if a path is vanilla:
    1. If the game has a vanilla manifest, checks exact membership.
    2. Fallback: Base game assets strictly reside under the 'audio/' root directory.
    3. Start going insane slowly...
    4. Are you checking my code?
    Simply compares music path against the checklist to decide if vanilla up or custom down.
    """
    clean_path = path.replace("\\", "/").strip().lower()

    if vanilla_manifest:
        return clean_path in vanilla_manifest

    # Any folder other than "audio/" is dynamically treated as a custom soundpack :)
    root_folder = clean_path.split("/", 1)[0]
    return root_folder == "audio"


def extract_tracks_from_txt(filepath: str, vanilla_manifest: set[str]) -> tuple[list[str], list[str]]:
    """
    Headphones List 3.
    Parses the audio pack, discovers custom folders dynamically,
    and returns (vanilla_tracks, custom_tracks) with order preserved and duplicates removed.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    matches = CACHE_REGEX.findall(content)
    if not matches:
        print(f"[!] Warning: No <<cacheaudio>> definitions found in '{filepath}'!")
        return [], []

    vanilla_raw: list[str] = []
    custom_raw: list[str] = []
    discovered_custom_folders: set[str] = set()
    illegal_chars = ("#", "?")

    for _, track_path in matches:
        clean_path = track_path.strip().replace("\\", "/")

        # TesterLan Rule Audits, I RULE OVER YOU! (jk I love you!)
        if any(char in clean_path for char in illegal_chars):
            print(f"[!] TL Warning: Audio path '{clean_path}' contains '#' or '?'! This WILL break in-game audio!!!")

        if "your audio here!" in clean_path.lower():
            print(f"[!] TL Warning: You forgot to replace the placeholder path: '{clean_path}'!")

        if is_vanilla_track(clean_path, vanilla_manifest):
            vanilla_raw.append(clean_path)
        else:
            custom_raw.append(clean_path)
            # Track the root folder name for the user
            root_dir = clean_path.split("/", 1)[0]
            discovered_custom_folders.add(root_dir)

    vanilla_unique = list(dict.fromkeys(vanilla_raw))
    custom_unique = list(dict.fromkeys(custom_raw))

    print("-" * 65)
    print(" DYNAMIC AUDIO DISCOVERY")
    print("-" * 65)
    if discovered_custom_folders:
        print(f"  • Custom Folder(s) Detected : {', '.join(sorted(discovered_custom_folders))}")
    print(f"  • Vanilla Tracks Identified : {len(vanilla_unique)}")
    print(f"  • Custom Tracks Identified  : {len(custom_unique)}")
    print("-" * 65 + "\n")

    return vanilla_unique, custom_unique


def generate_pocket_js(vanilla_tracks: list[str], custom_tracks: list[str]) -> str:
    """Builds the headphone setup.pocketMusicTracks array: Vanilla up, Custom down!!!"""
    lines: list[str] = ["setup.pocketMusicTracks = ["]

    if vanilla_tracks:
        lines.append("\t/* --- VANILLA TRACKS --- */")
        for track in vanilla_tracks:
            lines.append(f'\t"{track}",')

    if custom_tracks:
        lines.append("\t/* --- CUSTOM TRACKS --- */")
        for track in custom_tracks:
            lines.append(f'\t"{track}",')

    lines.append("];")
    return "\n".join(lines)


# =============================================================================
# MAIN PATCHER ROUTINE NNGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH~!
# =============================================================================

# --- Start Banner ---
print_banner()

# --- STEP 1: Find audio text file ---
audio_file = find_audio_file()
print(f"[•] Audio Pack   : {audio_file}")

try:
    with open(audio_file, "r", encoding="utf-8") as f:
        clean_text = f.read().strip()
except OSError as e:
    print(f"\n[!] Main Error: Failed to read '{audio_file}': {e}")
    input("Press Enter to exit...")
    sys.exit()


# --- STEP 2: Find game HTML file and handle backup safely bcuz they will kill me ---
html_file = find_html_file()
print(f"[•] Target Game  : {html_file}")

backup_file = html_file + ".bak"
if not os.path.exists(backup_file):
    shutil.copy2(html_file, backup_file)
    print(f"[✓] Safe Backup  : Created '{backup_file}'")
else:
    print(f"[i] Backup Check : Keeping existing clean backup '{backup_file}' safe.")

with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

print()

# --- STEP 3: Dynamically learn vanilla tracks from game & extract custom tracks owaaah?? ---
vanilla_manifest = extract_vanilla_manifest(html_content, backup_file)
vanilla_tracks, custom_tracks = extract_tracks_from_txt(audio_file, vanilla_manifest)


# --- STEP 4: Translate clean text to passage-safe HTML format, the only one thats literally easy to understand ---
ugly_text = (
    clean_text
    .replace("&", "&amp;")
    .replace("<", "&lt;")
    .replace(">", "&gt;")
    .replace('"', "&quot;")
    .replace("'", "&#39;")
)


# --- STEP 5: Define start and stop boundaries for passage BGM ---
start_pattern = re.compile(r"/\*\s*BGM\s*-\s*background music meant to be playe[rd]\s+on loop\s*\*/", re.IGNORECASE)
end_pattern = re.compile(r"/\*\s*BGV\s*-\s*voice sounds meant to be playe[rd]\s+on loop\s*\*/", re.IGNORECASE)

start_match = start_pattern.search(html_content)
end_match = end_pattern.search(html_content)

if not start_match:
    print("-" * 65)
    print("[!] Main Error: Could not find the BGM start marker!")
    print("[*] TesterLan Hint: Check DoL HTML using VS Code (If you have) and search for BGM or 'Mr Smith'")
    print("[*] TesterLan Hint: It could also mean your game version does not have audio somehow")
    print("\n[!] If this is an Issue, Please go over to Issues In LanVTester's Github.\n")
    print("-" * 65 + "\n")
    input("Press Enter to exit...")
    sys.exit()

if not end_match:
    print("-" * 65)
    print("[!] Main Error: Could not find the BGV stop marker!")
    print("[*] TesterLan Hint: Check DoL HTML using VS Code (If you have) and search for BGV or SFX")
    print("[*] TesterLan Hint: It could also mean your game version does not have audio somehow")
    print("\n[!] If this is an Issue, Please go over to Issues In LanVTester's Github.\n")
    print("-" * 65 + "\n")
    input("Press Enter to exit...")
    sys.exit()

start_pos = start_match.end()
end_pos = end_match.start()


# --- STEP 6: Surgically replace ONLY the BGM passage section, attack it like a doctor, speaking of doctor... MEDIC!!! ---
patched_content = (
    html_content[:start_pos]
    + "\n"
    + ugly_text
    + "\n\n"
    + html_content[end_pos:]
)


# --- STEP 7: Surgically update the Headphone (pocketMusicTracks) Library, OWAHHAHAHAAH ---
pocket_match = POCKET_REGEX.search(patched_content)
headphones_found = False

if pocket_match:
    headphones_found = True
    new_pocket_js = generate_pocket_js(vanilla_tracks, custom_tracks)
    patched_content = POCKET_REGEX.sub(lambda _: new_pocket_js, patched_content, count=1)
    print("[✓] Headphone Sync : 'setup.pocketMusicTracks' found and rebuilt dynamically!")
else:
    print("[i] Headphone Sync : 'setup.pocketMusicTracks' not found. Skipping playlist rebuild.")


# --- STEP 8: Atomic Save ---
temp_file = html_file + ".tmp"
try:
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(patched_content)
    os.replace(temp_file, html_file)
except OSError as e:
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print(f"\n[!] Error during save: {e}")
    input("Press Enter to exit...")
    sys.exit()


# --- STEP 9: Patch.py-chan Celebration Dialogues ---
print("\n" + "=" * 65)

if headphones_found:
    print(" SUCCESS: BGM and Headphone tracklists patched successfully!")
    print("=" * 65)
    print("\nAll Audio/Sfx were kept safe! Probably!\n")

    headphones_dialogues: list[list[str]] = [
        # Option 1 (TL Original)
        [
            "patch.py-chan: I LOVE YOU FOR USING ME! PLEASE PRAISE ME FOR DOING WORK!!!",
            "patch.py-chan: I updated both the area BGM and your headphone playlist! <3",
            "patch.py-chan: Vanilla is all on top, and custom is all on the bottom, just like you wanted!",
            "\nTL: she is not responsible if your headphone playlist broke somehow.\n",
            "patch.py-chan: uhmm what?",
            "patch.py-chan: Anyway! THANK YOU SENPAI!!!",
        ],
        # Option 2 (Hyperactive flexing / or showing off)
        [
            "patch.py-chan: LOOK SENPAI, LOOK! IT WORKED! PERFECT SYNC ON EVERYTHING!!",
            "patch.py-chan: BGM injected! Headphones sorted! Zero syntax errors! DID YOU SEE THAT?!",
            "\nTL: Nuh uh, you almost choked on that regex two seconds ago.\n",
            "patch.py-chan: SHUT UP TL, LET SENPAI BE IMPRESSED WITH ME!!",
            "patch.py-chan: See? You didn't even need Restore.py-chan today! I handled it all by myself!!",
            "patch.py-chan: PLEASE TELL ME I'M YOUR FAVORITE SCRIPT SENPAI! <3",
        ],
        # Option 3 (DJ energy / and taking credit)
        [
            "patch.py-chan: DJ PATCH.PY-CHAN IN THE HOUSE!!!!! All your tracks are live and ready!",
            "patch.py-chan: Vanilla on top, custom jams on deck, your headphones are officially blessed!!",
            "patch.py-chan: If your game sounds incredible right now, you know exactly who to thank~",
            "\nTL: how dare you? taking credit for music other people composed???\n",
            "patch.py-chan: I DELIVERED IT WITH LOVE, THAT COUNTS FOR AT LEAST 80%!!",
            "patch.py-chan: GO BLAST YOUR TUNES INTO YOUR HEAD SENPAI!! THANK YOU FOR BELIEVING IN ME!!!!!!",
        ],
    ]

    for line in random.choice(headphones_dialogues):
        print(line)

else:
    print(" SUCCESS: Main game BGM patched successfully!")
    print("=" * 65)
    print("\nAll Audio/Sfx were kept safe! Probably!\n")

    no_headphones_dialogues: list[list[str]] = [
        # Option 1 (TL Original)
        [
            "patch.py-chan: I LOVE YOU FOR USING ME! PLEASE PRAISE ME FOR DOING WORK!!!",
            "patch.py-chan: Um... senpai? I updated all your area BGM perfectly, but...",
            "patch.py-chan: I couldn't find the headphone playlist (setup.pocketMusicTracks) in your game!",
            "patch.py-chan: B-BUT THAT'S TOTALLY OKAY! You're probably playing a version without headphones or it's built different!",
            "patch.py-chan: Your main game music is 100% patched and ready, so don't worry your pretty head about it!",
            "patch.py-chan: PLEASE PRAISE ME ANYWAY SENPAI!!! <3",
        ],
        # Option 2 (Panick then coping)
        [
            "patch.py-chan: W-WAIT! Senpai, don't look at me like that, it's not my fault!!",
            "patch.py-chan: The main BGM is 100% patched, but your HTML didn't have headphone code in it!",
            "\nTL: Probably an older build or an unmodded pocket playlist.\n",
            "patch.py-chan: SEE?! TL agreed with me for once! It's not a bug, it's just your version!!",
            "patch.py-chan: Your area music is still good, so I still did an amazing job, right?!",
            "patch.py-chan: Don't run to Restore.py-chan, tell me I did good!! PLEASE SENPAI!!",
        ],
        # Option 3 (Dramatic sulking for headpats)
        [
            "patch.py-chan: *sniff* I searched everywhere for setup.pocketMusicTracks...",
            "patch.py-chan: I crawled through thousands of lines of SugarCube code just for you, senpai...",
            "\nTL: ...and you found nothing because their version doesn't use that long strings of variables.\n",
            "patch.py-chan: BUT I STILL INJECTED ALL THE MAIN BGM CLEANLY!! THAT STILL COUNTS!!",
            "patch.py-chan: You can still hear all your background tracks just fine!",
            "patch.py-chan: A whole 99% success rate is basically an A+, right?! PRAISE ME PLEASE!! <3",
        ],
    ]

    for line in random.choice(no_headphones_dialogues):
        print(line)

print("\n" + "=" * 65)
input("Press Enter to finish...")

# I'm the best aren't I? -TL <3