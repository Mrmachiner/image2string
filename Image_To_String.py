from PIL import Image
import pytesseract
import time
import cv2
start =time.time()

img = Image.open("/home/minhhoang/Pictures/e.png")
img.load()
abcd = cv2.imread("/home/minhhoang/Pictures/b.png")
cv2.imshow("abcd",abcd)

#pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(img,lang="kor")
end = time.time()

print(text)
print(end-start)
cv2.waitKey()