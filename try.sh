for file in Front_Images/*; do
	python3 OCR.py -f $file
done