"""20CS016 Vatsal Ghoghari"""
import img2pdf
from PIL import Image
import os
img_path = "result.png"
pdf_path = "result.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
