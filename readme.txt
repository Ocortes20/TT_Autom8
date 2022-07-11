Tiktok Reddit Automater

Automates story time style tiktok with tts for tiktok using moviepy, selenium, and other things.

FFMPEG and ChromeDriver must be installed

Instructions:

Step 1: $pip3 install -r requirements.txt
Step 2: Load up your assets folder with some background video and audio
Step 3: Change your main.py file to load the video you want to use (maybe I'll stick it into .env rn but idk)
Step 4: If you want to try out storytime videos or something diff, check out renderReddit.py for more video types. I see the main.py file as more of a sandbox for you to use the functions written.


Other comments:

- Sometimes the comment / audio in a video will not align. This is usually because the comment was deleted, and PSAW will not pick it up. I don't have a fix for it right now, perhaps someone can propose a change
- Sometimes there will be an error about decodeErrors, that can be either a blank entry, or something else
- The video might not be able to render every deleted post. I don't have a fix if PSAW can't pick it up. 
- There are some functions in textToSpeech.py and other places that are commented out using other technologies like azure, gtts, etc. I don't advise you use them, but if you want to try, the imports are there just pip install the appropriate dependencies.
- Videos end up in /videoGenerations/videos , you'll also find in tmp some assets for the video. You can clear out the tmp folder when the video is done rendering. Just don't delete the tmp folder (it's used in the rendering of the actual video).

Have fun with it. Enjoy, god bless, and stay safe!
