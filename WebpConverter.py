import glob, os
import moviepy.editor as moviepy
from PIL import Image

os.chdir("D:/DownloadsLesser/Meme")
for file in glob.glob("*.webp"):
    im = Image.open(file).convert("RGB")

    fnew = file.rsplit( ".", 1 )[ 0 ] 

    im.save(fnew + ".jpg","jpeg")

    os.remove( file )

for file in glob.glob("*.webm"):
    fNew = file.rsplit(".", 1 )[ 0 ]
    
    clip = moviepy.VideoFileClip(file)
    clip.write_videofile(fNew + '.mp4')

    os.remove( file )
    
