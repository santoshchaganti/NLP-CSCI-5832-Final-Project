# code adapted from https://pypi.org/project/pytesseract/
from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:

# IMPORTANT: change this to your tesseract install on your machine
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('img/test3.png')))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
print(pytesseract.image_to_string('img/test3.png'))

# List of available languages
print(pytesseract.get_languages(config=''))

# Test languages
print(pytesseract.image_to_string(Image.open('img/test-por.png'), lang='por'))
print(pytesseract.image_to_string(Image.open('img/test-hin.png'), lang='hin'))
print(pytesseract.image_to_string(Image.open('img/test-fas3.png'), lang='fas'))

# Batch processing with a single file containing the list of multiple image file paths
#print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
try:
    print(pytesseract.image_to_string('img/test.jpg', timeout=2)) # Timeout after 2 seconds
    print(pytesseract.image_to_string('img/test.jpg', timeout=0.5)) # Timeout after half a second
except RuntimeError as timeout_error:
    # Tesseract processing is terminated
    pass

# Get bounding box estimates
#print(pytesseract.image_to_boxes(Image.open('test3.png')))

# Get verbose data including boxes, confidences, line and page numbers
#print(pytesseract.image_to_data(Image.open('test3.png')))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open('test3.png')))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('img/test3.png', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default

# Get HOCR output
#hocr = pytesseract.image_to_pdf_or_hocr('test3.png', extension='hocr')

# Get ALTO XML output
#xml = pytesseract.image_to_alto_xml('test3.png')

# getting multiple types of output with one call to save compute time
# currently supports mix and match of the following: txt, pdf, hocr, box, tsv
text, boxes = pytesseract.run_and_get_multiple_output('img/test3.png', extensions=['txt', 'box'])