import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image
image = Image.open('/home/aryaman/Minor Project/WhatsApp Image 2024-05-07 at 12.13.13 PM.jpeg')

# Extract the text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
