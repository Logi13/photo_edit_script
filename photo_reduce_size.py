import os
from PIL import Image

inDirectory = r'C:/photos_in'
outDirectory = r'C:/photos_out'

# New Image parameters
newImageSize = 1500, 1500
newImageQuality = 75

# New Image settings
optimizeImage = True
resize = True

# New Image output type
outputType = ".jpg"

def resizeImage(image, newSize):
    # downsize the image with an ANTIALIAS filter (gives the highest quality)
    return image.resize(newSize, Image.Resampling.LANCZOS)

def convertImage(image):
    # If it is stored with transparence we need to remove the transparency as jpg does not support it
    if image.mode in ("RGBA", "P"):
        return image.convert("RGB")
    else:
        return image

def exportImage(image):
    image.save(outDirectory + '/' + fileNameClean + outputType, optimize=optimizeImage, quality=newImageQuality)
    

print("Files need to be in the directory: " + inDirectory)
print("Output will be generated in the directory: " + outDirectory)

print("Starting itterating directory...")
for subdir, dirs, files in os.walk(inDirectory):
    for filename in files:
        print("Converting file with name: " + filename)
        filepath = subdir + os.sep + filename
        fileNameClean = filename.rsplit('.', 1)[0]
        fileExtension = filename.rsplit('.', 1)[1]
        if filepath.endswith(".png"):
            try:
                im = Image.open(filepath)
                
                if resize:             
                    im = resizeImage(im, newImageSize)
                
                if outputType == ".jpg":
                    im = convertImage(im)

                exportImage(im)
            except Exception as e: 
                print("Error! Try again. Error: " + str(e))
        elif filepath.endswith(".jpg"):
            try:
                im = Image.open(filepath)

                if resize:             
                    resizeImage(im, newImageSize)
                
                exportImage(im)

            except Exception as e: 
                print("Error! Try again. Error: " + str(e))
        else:
            print("File Type not supported! For file with name: " + fileNameClean + " and file extension: " + fileExtension)