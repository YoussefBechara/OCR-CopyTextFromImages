import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def ocr_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    return text

# Test the function
image_path = r"C:\Users\user\Downloads\Screenshot_1-4-2024_12945_www.youtube.com.jpeg"
print(ocr_from_image(image_path))
