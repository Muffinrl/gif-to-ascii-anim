import append_text as at
import create_ascii_anim as caa
import frame_decompose as fd

def convert_gif_to_anim(file='target.gif', work='work', width=80):
    fd.gif_to_jpg(file, work)
    caa.generate_ascii_art_folder(work, 'animation.txt', width)
    
convert_gif_to_anim()

