# gif-to-ascii-anim
Converts a .gif file to an executable and .txt file to play the .gif as ASCII animation in the command prompt

I'm actively working on making it as easy to use as possible, for now, here is the crude methodology:

1. Gather your .gif of choice;
2. Name it "target.gif" and place it in the src folder;
3. Open the command line in the src folder;
4. Run the following command: py main.py;
5. If you get an error, make sure the src folder has an "in" folder and a "work" folder;
6. If main.py runs succesfully, you should get the message: "All frames saved as JPEG images in work."
7. Now you can run run.exe and it will display the animation in the command prompt.
