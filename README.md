# gif-to-ascii-anim
Converts a .gif file to an executable and .txt file to play the .gif as ASCII animation in the command prompt.

# HOW-TO-DOWNLOAD:
Download the following files from the latest release:
- ASCIIAnimator.exe
- run.exe

# HOW-TO-USE:
1. Obtain your .gif of choice;
2. Open ASCIIAnimator.exe and select your .gif file, you should see your gif show up in the application window;
3. Enter the width of your ASCII animation (somewhere around 80 is recommended as 80x32 makes nice looking animations);
4. Click "Convert to Animation", you should get a pop-up saying "Succesfully created animation.txt!";
5. The application will create an animation.txt file and a work folder with a frame-by-frame decomposition of your .gif, in case you need it;
6. Move the animation.txt into the same folder as your run.exe and then run run.exe.
7. You should see your animation displayed in the console
8. Enjoy :)

NOTE: run.exe will run whatever animation.txt is in the same directory as the executable
IF YOU DO NOT SEE YOUR ANIMATION, MAKE SURE YOU HAVE THE CORRECT ANIMATION.TXT

# Features in development:
- ASCII animation to .gif converter
- Frame editor (cropping out frames)
- ASCII movies (.mp4)
- Clean GUI
- Specifying framerate when playing back animations with run.exe
