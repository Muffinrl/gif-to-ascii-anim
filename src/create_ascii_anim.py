###
# create_ascii_anim.py creates a .txt animation file from a
# frame_decomposed .gif (see frame_decompose.py)
# frame_decompose.py is technically a dependency, unless you 
# have a hand_extracted folder of .gif frames.
###

import os
from PIL import Image

# Define the ASCII characters to represent different levels of gray
ASCII_CHARS = '&#%*/(.,  '

# Resize the image to the desired width while maintaining the height at 32 pixels
def resize_image(image, new_width=100):
    width, height = image.size
    new_height = 32
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to a grayscale value
def grayscale(image):
    return image.convert('L')

# Map each grayscale value to an ASCII character
def pixels_to_ascii(image, width):
    pixels = image.getdata()
    ascii_str = ''
    min_gray = min(pixels)
    max_gray = max(pixels)
    gray_range = max_gray - min_gray
    for i, pixel_value in enumerate(pixels):
        scaled_value = int((pixel_value - min_gray) / gray_range * (len(ASCII_CHARS) - 1))
        ascii_str += ASCII_CHARS[scaled_value]
        if (i + 1) % width == 0:  # Add newline after each row
            ascii_str += '\n'
    # Replace ":" characters with empty space
    ascii_str = ascii_str.replace(':', ' ')
    return ascii_str

# Convert a JPEG image to ASCII art
def jpeg_to_ascii(image_path, width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return None

    image = resize_image(image, width)
    image = grayscale(image)
    ascii_str = pixels_to_ascii(image, width)
    return ascii_str

# Loop over the JPEG files in a folder and generate ASCII art for each image in ascending order
def generate_ascii_art_folder(input_folder, output_file, width=100):
    ascii_art_combined = ""
    file_list = os.listdir(input_folder)
    file_list = sorted([file for file in file_list if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg')],
                       key=lambda file: int(file.split('_')[1].split('.')[0]))

    for file in file_list:
        image_path = os.path.join(input_folder, file)
        ascii_art = jpeg_to_ascii(image_path, width)
        if ascii_art is not None:
            ascii_art_combined += ascii_art + "\n\n"

    # Write the combined ASCII art to a .txt file
    with open(output_file, 'w') as file:
        file.write(ascii_art_combined)