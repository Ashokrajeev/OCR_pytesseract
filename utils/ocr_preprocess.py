'''

Usage on Command line to preprocess images only - Using Anaconda Prompt in the parent directory of all files

python ocr_preprocess -i image_name.jpg -p blur

i is for image and p is for preprocessing

'''
from PIL import Image
import pytesseract
import numpy as np
import argparse
import cv2, os

def remove_noise(image):
    return image
    return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)



# parse the argument
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="tmp.jpg")
parser.add_argument("-p", "--preprocess", type=str, default="blur")
args = vars(parser.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["file"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

methods = {}

gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
methods["thresh"] = remove_noise(gray)

gray = cv2.medianBlur(gray, 3)
methods["blur"] = remove_noise(gray)

gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

methods["adaptive"] = remove_noise(gray)

for val in methods.keys():

    # write the grayscale image to disk as a temporary file
    filename = "utils/"+val+".png".format(os.getpid())
    cv2.imwrite(filename, methods[val])

    # load the image as a PIL/Pillow image
    # apply OCR
    # delete temp image
    text = pytesseract.image_to_string(Image.open(filename))
    # os.remove(filename)

    # TO-DO : Additional processing such as spellchecking for OCR errors or NLP
    text = text.split("\n")
    f = open("utils/"+val+".txt","w")
    for line in text:
        if(len(line.strip()) > 0):
            print(line)
            f.write(line+"\n")
    f.close()
    print("\n\n************************\n\n")

