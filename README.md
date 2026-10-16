# CacheAudioShenanigans
CAS (CacheAudioShenanigans) - BGM &amp; Headphone Audio Patcher for Degrees of Lewdity Plus/X-Change.


--- TesterLan: I was lazy and just copy & pasted my tutorial below lol ---

step 0: literally have a PC or a LAPTOP!

step 1: have vscode or other coding software and a working computer
step 2: check cacheaudio.txt using vscode
step 3: add your own audio n stuff, if you were a python coder with trauma im pretty sure you can understand what to do there
step 3.3: add your copied audio to a folder or subfolder in special-audio-tl
step 3.5: copy ur audio file name in the folder and what format it is (e.g .opus) and add it to the custom track
step 3.6 notice: if a folder is missing in SATL then add it by checking the bgm folder name in the base audio game or just in the code.
step 4: take the three files (CacheAudio.txt and Patch.py and special-audio-tl) out of CacheAudioShenanigans
step 4.5: you can put back the cacheaudio.txt and patch.py in the folder again but do not put in the SATL, just leave it in the DoL Folder or it does not work, and do not put it in the audio folder too.
step 5: run patch.py using "python patch.py" in vscode terminal or run code in vscode
step 5.5: stop patch.py in vscode by pressing stop code or ctrl + c in the vscode terminal

step 6: congrats you did it without having to suffer HTML hell!
step 7: enjoyment and realize you WANT to add more audio.
step 7.1: spend 4 hours adding audio and finishing it.
step 7.5: suffer in enjoyment :)


for wanna play w custom music nubs:
step 0: pull out the 3 files (CacheAudio.txt and Patch.py and special-audio-tl from mediafire) in your DoL Folder (the one with the html file)
step 1: install python from microsoft store or on a trusted website
step 2: run patch.py using python
step 3: press enter to stop it
step 4: yay ur done!
step 5: you can go ahead and put back the (CacheAudio.txt and Patch.py) in the CAS Folder but leave the special-audio-tl in the DoL Folder

------------------------------------------------------------------------------------------------------------------------------------------

How to add your own track without blowing up everything into red!

step 1: become a python coder with trauma
step 2: go insane
step 3: go insane again
step 4: become afraid
step 5: actual start of tutorial
step 6.7: you may see something like this
---
            <<case "arcade">>
                <<cacheaudio "arcade1" "audio/bgm/arcade/HoliznaCC0 - Mutant Club.mp3">>

                <<cacheaudio "tl-arcade-1" "special-audio-tl/bgm/arcade/Oliver Buckland - incision.opus">>
                <<cacheaudio "tl-arcade-2" "special-audio-tl/bgm/arcade/Oliver Buckland - rapid_data_transfer.opus">>
                    <<createplaylist "arcade">>
                        <<track "arcade1">>

                        <<track "tl-arcade-1">>
                        <<track "tl-arcade-2">>
---
step 6.9: simply copy and paste the last track (like <<cacheaudio to last >>) and update the tl number and put in your new audio file name, dont forget the last one too you can find by rightclicking and checking properties! (e.g mp3, etc.)
step 7: try the same thing for the track tl one, copy and paste and update it to the current number of cacheaudio!
step 7.5: my example
---
            <<case "arcade">>
                <<cacheaudio "arcade1" "audio/bgm/arcade/HoliznaCC0 - Mutant Club.mp3">>

                <<cacheaudio "tl-arcade-1" "special-audio-tl/bgm/arcade/Oliver Buckland - incision.opus">>
                <<cacheaudio "tl-arcade-2" "special-audio-tl/bgm/arcade/Oliver Buckland - rapid_data_transfer.opus">>
                <<cacheaudio "tl-arcade-3" "special-audio-tl < real important do not confuse with "audio"/bgm/bgm area subfolder/hussrooms theme.opus">>
                    <<createplaylist "arcade">>
                        <<track "arcade1">>

                        <<track "tl-arcade-1">>
                        <<track "tl-arcade-2">>
                        <<track "tl-arcade-3">>
---
step 7.55: get it?
step 7.75: ok from this point onwards you can learn the great ways of code and how it hurts soon!

step 7.77: if your wondering where mr smith - dusk is in my SATL, uhmm I kinda deleted it because I HATED the music and you should too when you listen to it multiple times when testing audio in-game


step 7.775: use ctrl + h for find and replace, or be simple by using f3 instead. 

------------------------------------------------------------------------------------------------------------------------------------------
Extra Thing about the .Bak that is created in your DoL Folder, if your DoL's Main HTML File Breaks, You can switch the .bak to .html and send that broken DoL to the Trash! But you should try to find the cause of what broke your game tho.

In simple terms, | .html.bak | > what you see when it creates a copy. Remove the .bak simply

Can't find and know how to edit .file?
Go to explorer, find "view", go over to "show", click file name extensions.




OR YOU CAN BE A LAZY IDIOT AND USE MY RESTORE SCRIPT! (restore.py)
just make sure you move the original html or you can't guess which one is restored... hmph...



did i mention you can also pick up the .txt and put it on the patch.py so it works?
same for restore.py just pick up the .bak and put it on the restore.py :)



important rules for audio: do not add an audio file with a name that has a # symbol in it or a ? symbol or else it will not work ingame. (you can just edit the file name to not have an excluded symbol in the SATL or ur custom audio, all else works.)


this has been only tried In DoL X-Change!!! so I dont know about the other versions like Vanilla DoL or other mods. <~< -TL


uhm thats what I can do mostly in my current knowledge, ask someone else in DoL modding discord or smth, this is your responsibility depending on ur coding intelligence or knowing what to do.

also im not updating this anymore unless I get an error on my own pc or lowk feel like it, you hereby automatically agree on reading this CAS.txt that if you break ur code somehow, that is and will be your fault!

I know there is a sfx/bgv area, I just refuse to expand my code to it, let em superdevs do it, im lazy okay? > to whoever is reading this



(Cache-Audio - Your Template + No Vanilla.txt or its vanilla version can be anything, like Cache-Audio(NON-V)_Monogatari Overhaul_v???.txt lol ngl I would love for it to exist soon maybe..)


Is it me or Is the intructions just chaotic?


patch.py fixes your audio onto the main game, and patch the headphones aswell. I didnt know there were headphones in the game lol... its in high street in shopping centre in the furniture store and electronics
might be niche or smth.
also I do not know if this is in the vanilla game DoL lol.

Meow!

I do not know where bgm/home even goes to, it certainly isnt in the orphanage pc room, or smth.. is there even a radio in the game orrrr am i schizo? probably schizo totally

|----TesterLan----|


T---T
for special custom modding on my behalf!

if ppl ever decide to make a dedicated music mod it should have a Cache-Audio_Name.txt and It's Custom Audio Folder In its zipfile.
all patch.py and restore.py should be only from me (LanVTester / TL CAS MOD) as to prevent some sort of bad actor secretly messing with my code.py in their custom zipfile.

also I, TL does have a discord account! I just refuse to tell you :)
u can say smth through the issues, tell me if the game updated and somehow broke my code (and I can find it or replicate) or they literally added new audio locations so tell me In Issues and I can fix my template and add some folders.

[also I do not check my github that often so something like every some lucky week]
T---T
