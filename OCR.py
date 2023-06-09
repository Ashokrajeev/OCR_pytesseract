import pytesseract
from pytesseract import Output
import cv2
from PIL import Image
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True , help = "Path to file" )
parser.add_argument("-o", "--output", required=False , help = "Output file" )
# parser.add_argument("-p", "--preprocess", type=str, default="blur",choices = ["blur","thresh","adaptive"])

args = parser.parse_args()

import shutil

shutil.copyfile(args.file, "utils/tmp.jpg")


exec(open("utils/crop_morphology.py").read())
# print("Cropped")
exec(open("utils/deskew.py").read())
# print("Rotated")
exec(open("utils/ocr_preprocess.py").read())
# print("Preprocessed")

os.remove("utils/tmp.jpg")

os.rename("utils/Output.txt", args['file']+".txt")
# os.remove("utils/thresh.txt")
# os.remove("utils/adaptive.txt")
# os.rename('utils/blur.txt', "utils/"+args['file'].split("/")[-1]+".txt")