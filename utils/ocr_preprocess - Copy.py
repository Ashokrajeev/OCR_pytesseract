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

# parse the argument
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="tmp.jpg")
parser.add_argument("-p", "--preprocess", type=str, default="blur")
args = vars(parser.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["file"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check preprocess to apply thresholding on the image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 3)

elif args["preprocess"] == "adaptive":
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

# write the grayscale image to disk as a temporary file
filename = "tmp2.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image
# apply OCR
# delete temp image
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

# TO-DO : Additional processing such as spellchecking for OCR errors or NLP
text = text.split("\n")
print("Got ",args['preprocess'])
f = open(args['preprocess']+".txt","w")
f.close()
for line in text:
    if(len(line.strip()) > 0):
        print(line)

# show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite('img.jpg', thresh1)
# extracted_text = pytesseract.image_to_string(thresh1,lang = 'eng')
# if(args.output == None):
#   print(extracted_text)
# else:
#   f = open(args.output,"a")
#   f.write(extracted_text+"\n")
#   f.close()