import pytesseract
from pytesseract import Output
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True , help = "Path to file" )
parser.add_argument("-o", "--output", required=False , help = "Output file" )

args = parser.parse_args()

img = cv2.imread(args.file)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
# img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Sobel Edge Detection
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# cv2.imwrite('img.jpg', img_gray)
extracted_text = pytesseract.image_to_string(img)
if(args.output == None):
	print(extracted_text)
else:
	f = open(args.output,"a")
	f.write(extracted_text+"\n")
	f.close()