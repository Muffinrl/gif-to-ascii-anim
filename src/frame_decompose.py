###
# frame_decompose.py takes a .gif as input, described by
# the gif_file variable. It then outputs the frames of which
# the file is composed as jpeg images.
###

from PIL import Image

def gif_to_jpg(gif_path, output_folder):
    # Open the .gif file
    gif = Image.open(gif_path)

    # Iterate over each frame in the .gif
    for frame_num in range(gif.n_frames):
        # Seek to the current frame
        gif.seek(frame_num)

        # Convert the frame to RGBA mode
        frame_rgba = gif.convert('RGBA')

        # Create a new white background image
        background = Image.new('RGBA', gif.size, (255, 255, 255))

        # Create composed image from the frame onto the background using alpha composite
        composed = Image.alpha_composite(background, frame_rgba)

        # Convert the composed image to RGB mode and remove transparency
        frame_rgb = composed.convert('RGB')

        # Save the frame as a JPEG image
        output_path = f"{output_folder}/frame_{frame_num}.jpg"
        frame_rgb.save(output_path, 'JPEG')

    print(f"All frames saved as JPEG images in {output_folder}.")