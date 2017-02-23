# videomaker
A short python video maker from a picture and an audioclip

Usage
```
pip install -r requirements.txt
```
You might need to download some additional codecs then
```
NeedDownloadError: Need ffmpeg exe. You can download it by calling:
  imageio.plugins.ffmpeg.download()
```
```
First (sudo) pip install imageio, if necessary.
Now: import imageio and then imageio.plugins.ffmpeg.download()
```

```
python app.py -a example.wav -i example.jpg -o output.avi
```
You run the script and give -a for Audio file -i for Image file and -o for Output file
## you can also use long long-style option names like --audiofile --imagefile --ouputfile


#Audio files tested:
    *.mp3 
    *.wav
#Image files tested:
    *.jpg, *.jpeg
    
**Output file should be ending on *.avi or you might need to add some codec**
