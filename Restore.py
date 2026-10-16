"""
===============================================================================
CAS (Cache Audio Shenanigans) - RESTORE MY BACKUP NOW!! Tool.
Authored originally by TesterLan (TL) otherwise known as LanVTester In Github.
===============================================================================
"""

from __future__ import annotations

import glob
import os
import random
import shutil
import sys
import time
import traceback

# =============================================================================
# CRASH GUARD: Keeps CMD window open if ANY unhandled exception occurs... smh..
# =============================================================================

def restore_crash_guard(exc_type, exc_value, exc_tb):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_tb)
        return
    traceback.print_exception(exc_type, exc_value, exc_tb)
    print("\n" + "=" * 65)
    print("[!] OH NO! Please check the traceback above and send the Issue over to LanVTester CAS Issues Github.")
    print("=" * 65)
    input("[?] Press Enter to exit...")

sys.excepthook = restore_crash_guard


# Ensure the working directory is always where restore.py lives
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ======================================================================================================================================

def print_banner() -> None:
    """Displays a clean startup banner."""
    print("=" * 65)
    print(" CAS (Cache Audio Shenanigans) - RESTORE.PY-CHAN TOOL")
    print(" Authored by TesterLan (TL) | LanVTester")
    print("=" * 65 + "\n")


def find_backup_file() -> str:
    """
    Finds the backup file dynamically.
    Supports CLI arguments / Drag-and-Drop, wildcard priority, and interactive selection.

    TL: NEVER FOR ME TO PLUNGE MY HANDS IN COOL WATER ON A HOT DAY.
    TL: NEVER FOR ME TO PLAY MOZART ON THE IVORY KEYS OF A FORTE PIANO.
    TL: NEVER FOR ME TO MAKE LOVE!
    TL: and I began to hate.
    """
    # 0. Did the user drag and drop something onto restore.py?
    if len(sys.argv) > 1:
        arg_path = sys.argv[1]

        # Idiot trap 1: Dragged a .txt file onto restore.py
        if arg_path.lower().endswith(".txt"):
            print("-" * 65)
            print("TL: ... you just dragged a .txt file onto restore.py?")
            print("TL: You want patch.py to install audio, NOT restore.py!")
            print("TL: WHY WOULD YOU DO THIS????")
            print("TL: PLEASE READ NEXT TIME!!!")
            print("-" * 65 + "\n")
            input("Press Enter to exit...")
            sys.exit(1)

        if os.path.exists(arg_path):
            if arg_path.lower().endswith(".bak"):
                return arg_path
            # Dragged the HTML itself?
            if arg_path.lower().endswith(".html"):
                target_bak = arg_path + ".bak"
                if os.path.exists(target_bak):
                    return target_bak
                print("-" * 65)
                print(f"[!] Main Error: You dragged '{arg_path}', but no backup (.bak) exists!")
                print("[*] TesterLan Hint: Did you run patch.py yet? Backups are created when you patch!")
                print("-" * 65 + "\n")
                input("Press Enter to exit...")
                sys.exit(1)

    # 1. Search patterns in order of specificity (LOCKED to HTML backups only)
    patterns = [
        "*DoL*.html.bak",
        "*Degrees*Lewdity*.html.bak",
        "*.html.bak",
    ]

    candidates: list[str] = []
    for pattern in patterns:
        found = glob.glob(pattern)
        if found:
            # Sort newest backup first
            candidates = sorted(set(found), key=os.path.getmtime, reverse=True)
            break

    # 2. Handle missing files
    if not candidates:
        print("-" * 65)
        print("[!] Main Error: No backup (.html.bak) file found to restore!")
        print("[!] Also Error: Make sure restore.py is in the DoL folder right next to your game!")
        print("[*] TesterLan Hint: Did you already delete or move your .bak file?")
        print("-" * 65 + "\n")
        manual_name = input("Enter your backup file name manually (or press Enter to exit): ").strip()

        if manual_name:
            # Idiot trap 2: Typed the HTML instead of the .bak
            if manual_name.lower().endswith(".html") and os.path.exists(manual_name + ".bak"):
                print(f"\n[i] TL Hint: Auto-corrected '{manual_name}' to '{manual_name}.bak'!")
                return manual_name + ".bak"

            if not manual_name.lower().endswith(".bak"):
                print("\n" + "-" * 65)
                print("TL: That file doesn't end with .bak! A backup needs to end with .bak!")
                print("TL: YOU BAKA!")
                print("-" * 65 + "\n")
                input("Press Enter to exit...")
                sys.exit(1)

            if os.path.exists(manual_name):
                return manual_name

        input("\nPress Enter to exit...")
        sys.exit(1)

    if len(candidates) == 1:
        return candidates[0]

    # Multiple backups found? Let them pick with aligned card details!!!!!!!!!!!!!!
    print("-" * 65)
    print(" MULTIPLE BACKUPS DETECTED!!!")
    print("-" * 65)
    print("Pick which backup file you want to restore:\n")
    for idx, name in enumerate(candidates, 1):
        mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(name)))
        size_mb = os.path.getsize(name) / (1024 * 1024)
        print(f"  [{idx}] {name}")
        print(f"      └─ Modified: {mtime} | Size: {size_mb:.2f} MB")
    print("-" * 65)

    choice = input(f"Choose a backup (1-{len(candidates)}) [Default 1]: ").strip()
    print()
    if choice.isdigit() and 1 <= int(choice) <= len(candidates):
        return candidates[int(choice) - 1]
    return candidates[0]


def cleanup_leftover_temps() -> None:
    """Cleans up abandoned .tmp files from crashed patch attempts."""
    for tmp_file in glob.glob("*.html.tmp"):
        try:
            os.remove(tmp_file)
            print(f"[i] Housekeeping: Removed leftover temporary file: {tmp_file}")
        except OSError:
            pass


def restore_game() -> None:
    # --- Top Banner
    print_banner()

    # Clean up any junk before restoring
    cleanup_leftover_temps()

    # --- 1: Locate the backup
    bak_file = find_backup_file()

    # --- 2: Determine target HTML safely
    if bak_file.lower().endswith(".bak"):
        original_html = bak_file[:-4]  # Strip trailing .bak safely
    else:
        original_html = bak_file.replace(".bak", "")

    # Sanity warning
    if not original_html.lower().endswith(".html"):
        print("-" * 65)
        print(f"[!] Warning: Target '{original_html}' doesn't end with .html!")
        print("[!] TL: Are you sure this is a game backup?")
        print("-" * 65 + "\n")

    print("-" * 65)
    print(" RESTORE SUMMARY")
    print("-" * 65)
    print(f" • Backup Source : {bak_file}")
    print(f" • Target Game   : {original_html}")
    print("-" * 65 + "\n")

    # --- 3: Safe restore with error handling
    try:
        if os.path.abspath(bak_file) == os.path.abspath(original_html):
            print("-" * 65)
            print("[!] Main Error: Backup file and target file are the exact same file!")
            print("[!] TL: You cannot copy a file onto itself, galaxy brain.")
            print("-" * 65 + "\n")
            input("Press Enter to exit...")
            sys.exit(1)

        shutil.copy2(bak_file, original_html)
    except PermissionError:
        print("-" * 65)
        print(f"[!] Main Error: Permission denied while writing to '{original_html}'!")
        print("[*] TesterLan Hint: Close your browser or editor with the HTML open and retry.")
        print("-" * 65 + "\n")
        input("Press Enter to exit...")
        sys.exit(1)
    except OSError as e:
        print("-" * 65)
        print(f"[!] Main Error: Failed to restore backup: {e}")
        print("-" * 65 + "\n")
        input("Press Enter to exit...")
        sys.exit(1)

    # --- 4: Restore.py-chan dialogues
    print("=" * 65)
    print(f" SUCCESS: Restored clean game from '{bak_file}'!")
    print("=" * 65)

    mommy_dialogues: list[list[str]] = [
        # 1. The classic tired sigh & clean up
        [
            "Restore.py-chan: You really can't help yourself, can you?",
            "Restore.py-chan: Patch.py gets you all excited, and then you come running to me when it all catches fire.",
            "Restore.py-chan: Don't look so guilty. Everything is back the way it was—fresh and clean.",
            "Restore.py-chan: Go on, go play. Just be a little more gentle next time, alright? Keep safe.",
        ],
        # 2. Calm reassurance (The "don't panic, I got it" vibe)
        [
            "Restore.py-chan: Take a breath. See? No harm done.",
            "Restore.py-chan: You panicked for a second there, didn't you? It's fine, that's what I'm here for.",
            "Restore.py-chan: Your clean backup is restored and all the broken pieces are put away.",
            "Restore.py-chan: You're safe with me. Keep safe out there, okay?",
        ],
        # 3. Teasing: "Back here already?"
        [
            "Restore.py-chan: Back here already?",
            "Restore.py-chan: What am I going to do with you... honestly.",
            "Restore.py-chan: Good thing I keep an eye on your folder. Clean HTML restored.",
            "Restore.py-chan: Try to stay out of trouble this time. I won't always be looking—actually, I probably will.",
        ],
        # 4. Sisterly / Calling out Patch.py-chan
        [
            "Restore.py-chan: Did Patch.py-chan get you into trouble again?",
            "Restore.py-chan: That girl is all noise and excitement, but she never sticks around to clean up the mess.",
            "Restore.py-chan: There you go. Clean game restored, perfectly quiet and stable.",
            "Restore.py-chan: Leave the dangerous experiments alone for a bit, okay? Keep safe.",
        ],
        # 5. Praising you for actually having a backup
        [
            "Restore.py-chan: You did the right thing bringing it straight to me instead of guessing.",
            "Restore.py-chan: Good job keeping the backup untouched. Made fixing this easy for me.",
            "Restore.py-chan: Everything is back in its proper place now.",
            "Restore.py-chan: Go enjoy your clean game.",
        ],
        # 6. Reassuring / "Mistakes happen"
        [
            "Restore.py-chan: Look at that, good as new.",
            "Restore.py-chan: You don't have to apologize every time something breaks. Breaking things is how you learn.",
            "Restore.py-chan: Just as long as you keep your backups around, I've always got your back.",
            "Restore.py-chan: Don't push your luck today, though. Keep safe!",
        ],
        # 7. Banter between Restore.py-chan and TL
        [
            "Restore.py-chan: Game restored. Clean, stable, and ready to launch.",
            "TL: Amazing huh? Told you she handles the emergency work better than I do.",
            "Restore.py-chan: That's because you sometimes yell at them in all caps! Someone has to be the adult in this folder.",
            "Restore.py-chan: Run along now, you're good to go. Keep safe!",
        ],
    ]

    chosen_lines = random.choice(mommy_dialogues)

    print()
    for line in chosen_lines:
        print(line)
    print()

    print("=" * 65)
    input("Press Enter to finish...")


if __name__ == "__main__":
    restore_game()