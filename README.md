# 🎧 CacheAudioShenanigans (CAS)
> **BGM & Headphone Audio Patcher for *Degrees of Lewdity X-Change*.**

[![Game](https://img.shields.io/badge/Game-Degrees%20of%20Lewdity%20X--Change-e60026?style=for-the-badge)](https://dolmods.net)
[![Engine](https://img.shields.io/badge/Engine-SugarCube%202-99001a?style=for-the-badge)](https://www.motoslave.net/sugarcube/2/)
[![Creator](https://img.shields.io/badge/By-TesterLan%20(TL)-ff1a40?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-330008?style=for-the-badge)](LICENSE)

---

> [!CAUTION]
> ### 🔗 Mediafire Link for TL's Audio: *Soon Maybe...*
> *My data provider decided to stop working when it was so CLOSE to uploading bro. Eventually I will genuinely skin my provider and turn them into a lamp shade.*

*Is it me or are the instructions below are just not chaotic like last time? guh (+----- TesterLan: I was lazy and used to just copy & pasted my tutorial below lol -----+)*

---

## ⚡ The Easiest Steps (Recommended `.exe` Method)
*No Python installation or coding software needed!*

1. **Download:** Grab the latest `.zip` of **CAS** and the latest **DoLX** `.zip` from [dolmods](https://dolmods.net).
2. **Unzip:** Extract both folders.
3. **Grab the Files:** Open the CAS `exe` folder and move these **3 things** into your main **DoLX folder** (the folder where your `.html` game file lives):
   * `patch.exe`
   * `cache-audio.txt` (or your template `.txt`)
   * Your custom audio folder (e.g., `special-audio-tl`)
4. **Patch It:** Run **`patch.exe`**.
5. **Done!** That's literally all. *(Note: `restore.exe` is only there to restore your previous `.html` of DoLX if something goes wrong).*

> [!TIP]
> **Drag & Drop Shortcut:** Did I mention you can literally just pick up your `.txt` file and drag-and-drop it directly onto `patch.py` / `patch.exe` so it works? Same for `restore.py`—just drag the `.bak` file onto `restore.py` :)

---

## 🐍 For "Wanna Play w/ Custom Music" Nubs (Python Method)
*If you want to use the `.py` scripts instead of the `.exe`:*

* **Step 0:** Pull out the 3 files (`CacheAudio.txt`, `patch.py`, and `special-audio-tl` from Mediafire) and put them in your **DoLX Folder** (the one with the `.html` file).
* **Step 1:** Install Python from the Microsoft Store or [python.org](https://www.python.org/).
* **Step 2:** Run `patch.py` using Python.
* **Step 3:** Press `Enter` to close it when it finishes.
* **Step 4:** Yay ur done!
* **Step 5:** You can put `CacheAudio.txt` and `patch.py` back into the CAS folder to keep things tidy, **but LEAVE `special-audio-tl` in the main DoLX folder!**

<details>
<summary><b>📜 Click to view the Outdated v0 Steps (For Historical Trauma & VS Code Nerds)</b></summary>
<br>

*(I just wanna say that the steps below are outdated since v0 so you can ignore them if you want, kept here to see).*

* **step 0:** literally have a PC or a LAPTOP!
* **step 1:** have vscode or other coding software and a working computer
* **step 2:** check `cacheaudio.txt` using vscode
* **step 3:** add your own audio n stuff, if you were a python coder with trauma im pretty sure you can understand what to do there
* **step 3.3:** add your copied audio to a folder or subfolder in `special-audio-tl` (or your own edited folder name)
* **step 3.5:** copy ur audio file name in the folder and what format it is (e.g `.opus`) and add it to the custom track in the code
* **step 3.6 notice:** if a folder is missing in SATL then add it by checking the bgm folder name in the base audio game or just in the code.
* **step 4:** take the three files (`CacheAudio.txt`, `Patch.py`, and `special-audio-tl`) out of `CacheAudioShenanigans`
* **step 4.5:** you can put back the `cacheaudio.txt` and `patch.py` in the folder again **but do not put in the SATL**, just leave it in the DoL Folder or it does not work, and do not put it in the base `audio` folder either.
* **step 5:** run `patch.py` using `python patch.py` in vscode terminal or run code in vscode
* **step 5.5:** stop `patch.py` in vscode by pressing stop code or `ctrl + c` in the vscode terminal
* **step 6:** congrats you did it without having to suffer HTML hell!
* **step 7:** enjoyment and realize you WANT to add more audio.
* **step 7.1:** spend 4 hours adding audio and finishing it.
* **step 7.5:** suffer in enjoyment :)

</details>

---

## 🔥 How to Add Your Own Tracks (Without Blowing Everything Up Into Red!)

* **= step 1:** become a python coder with trauma
* **= step 2:** go insane
* **= step 3:** go insane again
* **= step 4:** become afraid
* **= step 5:** *actual start of tutorial*

### = step 6.7: You will see something like this in `cache-audio.txt`:
```twee
            <<case "arcade">>
                <<cacheaudio "arcade1" "audio/bgm/arcade/HoliznaCC0 - Mutant Club.mp3">>

                <<cacheaudio "tl-arcade-1" "special-audio-tl/bgm/arcade/Oliver Buckland - incision.opus">>
                <<cacheaudio "tl-arcade-2" "special-audio-tl/bgm/arcade/Oliver Buckland - rapid_data_transfer.opus">>
                    <<createplaylist "arcade">>
                        <<track "arcade1">>

                        <<track "tl-arcade-1">>
                        <<track "tl-arcade-2">>
```

### = step 6.9: Copy & Paste the `<<cacheaudio>>` line
Simply copy and paste the last track (like `<<cacheaudio "tl-arcade-2"...>>`), update the `tl` number to `3`, and put in your new audio file name. **Don't forget the file extension at the very end!** (You can find it by right-clicking your song file $\to$ *Properties*, e.g., `.mp3`, `.opus`, `.m4a`).

### = step 7: Update the Playlist `<<track>>`
Do the exact same thing under `<<createplaylist>>`—copy and paste the last `<<track>>` line and update its number to match your new `cacheaudio` track!

### = step 7.5: My Example:
```twee
            <<case "arcade">>
                <<cacheaudio "arcade1" "audio/bgm/arcade/HoliznaCC0 - Mutant Club.mp3">>

                <<cacheaudio "tl-arcade-1" "special-audio-tl/bgm/arcade/Oliver Buckland - incision.opus">>
                <<cacheaudio "tl-arcade-2" "special-audio-tl/bgm/arcade/Oliver Buckland - rapid_data_transfer.opus">>
                <<cacheaudio "tl-arcade-3" "special-audio-tl/bgm/arcade/hussrooms theme.opus">>
                    <<createplaylist "arcade">>
                        <<track "arcade1">>

                        <<track "tl-arcade-1">>
                        <<track "tl-arcade-2">>
                        <<track "tl-arcade-3">>
```
*(⚠️ **REAL IMPORTANT:** Make sure the path starts with `special-audio-tl`—do NOT confuse it with the vanilla `"audio"` folder!)*

* **= step 7.55:** get it?
* **= step 7.75:** ok from this point onwards you can learn the great ways of code and how it hurts soon!
* **= step 7.77:** *If you're wondering where `mr smith - dusk` is in my SATL... uhmm I kinda deleted it because I HATED the music, and you would too if you had to listen to it 500 times while testing audio in-game.*
* **= step 7.775:** Use `Ctrl + H` for Find & Replace, or be simple by using `F3` instead.

---

> [!CAUTION]
> ### 🚫 IMPORTANT RULES FOR AUDIO FILENAMES
> **DO NOT** add an audio file with a name that has a **`#` (hashtag)** symbol or a **`?` (question mark)** symbol in it, or else **it will blow up into a red error box in-game!**
> 
> *(Just rename the audio file in your folder so it doesn't have `#` or `?` in the name. All other symbols work fine!)*

---

## 🛠️ Backups & Restoring (`.bak` & `restore.py`)

When you patch your game, CAS automatically creates a `.bak` backup file in your DoL folder. 
If your DoL's main HTML file ever breaks, you can fix it two ways:

### Method 1: The Manual Way
In simple terms, `| .html.bak |` is the backup copy created before patching. 
1. Send the broken `.html` file to the Trash.
2. Rename the `.html.bak` file by simply removing `.bak` at the end so it becomes `.html` again! *(You should still try to find what broke your game tho).*

> **Can't see `.bak` or `.html` at the end of your files?**  
> Open Windows File Explorer to click **View** at the top then click over **Show** and check **File name extensions**.

### Method 2: The Lazy Idiot Way (`restore.py` / `restore.exe`)
**OR YOU CAN BE A LAZY IDIOT AND USE MY RESTORE SCRIPT!**  
Just run `restore.py` (or drag your `.bak` file onto it).  
*hmph...*

---

## 💭 Random Lore, Notes & Disclaimers

* **DoLX Only:** This has **only** been tested in **DoL X-Change**!!! I don't know about other versions like Vanilla DoL or other mods. `<~< -TL`
* **Headphones Exist?!** `patch.py` fixes your audio onto the main game AND patches the in-game headphones as well. I didn't even know there were headphones in the game lol... they're on High Street in the Shopping Centre (inside the furniture/electronics store). Might be niche or smth. No idea if that's in vanilla DoL lol.
* **Where is `bgm/home`?** I do not know where `bgm/home` even goes to. It certainly isn't in the orphanage PC room, or smth... is there even a radio in the game orrrr am I schizo? Probably schizo totally.
* **No SFX / BGV:** I know there is an `sfx` / `bgv` (voice) area in the code. I just refuse to expand my code to it. Let 'em superdevs do it, I'm lazy okay? *(> to whoever is reading this).*
* **Custom Templates:** *(A `Cache-Audio - Your Template + No Vanilla.txt` or its vanilla version can be named anything, like `Cache-Audio(NON-V)_Monogatari Overhaul_v???.txt` lol ngl I would love for that to exist soon maybe...)*

> [!IMPORTANT]
> ### ⚖️ The "It's Your Fault" Agreement
> That's mostly what I can do with my current knowledge—ask someone else in the DoL Modding Discord or smth if you get stuck. This is your responsibility depending on your coding intelligence.
> 
> Also, I'm not updating this anymore unless I get an error on my own PC or lowk feel like it. **You hereby automatically agree upon reading this README that if you break your code somehow, that is and will be your fault!**

---

## 🛡️ Rule for Music Sub-Modders (`T---L`)

If people ever decide to make a dedicated music pack/mod using this tool:
1. Your zip file should **only** contain your `Cache-Audio_Name.txt` and your **Custom Audio Folder**.
2. **All `patch.py` / `restore.py` (and `.exe`) files should ONLY be downloaded directly from me (`LanVTester` / `TL CAS MOD`)** to prevent bad actors from secretly messing with my `.py` code inside their custom zip files.

---

### 📬 Contact & Bug Reports
* Yes, I, **TL**, do have a Discord account! **I just refuse to tell you :)**
* If a game update breaks my code (and I can replicate it), or if they literally added new audio locations to the game, tell me in the **GitHub Issues** tab so I can fix my template and add the new folders.
* *[Also I do not check my GitHub that often, so expect a reply every some lucky week]*

**Meow!**  
**|----TesterLan----| (`T---L`)**
