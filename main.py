# import all needed moduls
from moviepy.editor import *

# loading video
clip = VideoFileClip("myvid.mp4")

# getting only 3 first seconds from video
clip = clip.subclip(0, 3)

# saving video clip as gif
clip.write_gif("mygif.gif")

# loading gif
gif = VideoFileClip("mygif.gif")

# showing gif
gif.ipython_display()
