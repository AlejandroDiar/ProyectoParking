import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'

placa = []
image=cv2.imread('ejemplo1.png')

cv2.imshow('Image',image)
