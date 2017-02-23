import wave
import contextlib
import sys
import getopt
from moviepy.editor import AudioFileClip
from moviepy.video.VideoClip import ImageClip

audiofile = 'No audiofile'
imagefile = 'No imageFile'
outputfile = 'output.avi'

try:
    opts, args = getopt.getopt(sys.argv[1:], "ha:i:o:", ["afile=", "ifile" "ofile="])
except getopt.GetoptError:
    print ('app.py -a <audiofile> -i <imagefile> -o <outputfile>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('app.py -a <audiofile> -i <imagefile> -o <outputfile>')
        sys.exit()
    elif opt in ("-a", "--afile"):
        audiofile = arg
    elif opt in ("-i", "--ifile"):
        imagefile = arg
    elif opt in ("-o", "--ofile"):
        outputfile = arg

with contextlib.closing(wave.open(audiofile, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)

audioclip = AudioFileClip(audiofile)
myclip = ImageClip(imagefile, duration=duration)
full_video = myclip.set_audio(audioclip)
full_video.write_videofile(outputfile, codec='libx264', fps=24)
