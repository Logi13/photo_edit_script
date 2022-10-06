import os
from PIL import Image

inDirectory = r'C:/photos_in'
outDirectory = r'C:/photos_out'

print("Files need to be in the directory: " + inDirectory)
print("Output will be generated in the directory: " + outDirectory)

print("Starting itterating directory...")
for subdir, dirs, files in os.walk(inDirectory):
    for filename in files:
        print("Converting file with name: " + filename)
        filepath = subdir + os.sep + filename
        fileNameClean = filename.rsplit('.', 1)[0]
        if filepath.endswith(".png"):
            try:
                im = Image.open(filepath)
                if im.mode in ("RGBA", "P"): im = im.convert("RGB")

                # downsize the image with an ANTIALIAS filter (gives the highest quality)
                im = im.resize((1500,1500),Image.ANTIALIAS)
                im.convert('RGB')

                # im.save(outDirectory + '/' + filename + '.jpg', quality=75)  # The saved downsized image size is 24.8kb

                im.save(outDirectory + '/' + fileNameClean + '.jpg', optimize=True, quality=75)  # The saved downsized image size is 22.9kb
            except Exception as e: 
                print("Error! Try again. Error: " + str(e))