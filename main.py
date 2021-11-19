# importing the module
import os

import cv2
import pytesseract
from googletrans import Translator
from gtts import gTTS
import pyttsx3
engine = pyttsx3.init()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# reading the video
source = cv2.VideoCapture('vd.mp4')
source.set(3,640)
source.set(4,480)

# running the loop
while True:

    # extracting the frames
    ret, img = source.read()

    # converting to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.threshold(gray, 0, 255,
                         #cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #blur to avoid noise
    gray = cv2.medianBlur(gray,1)
    #gray = cv2.bilateralFilter(gray, 10, 60, 50)
    #threshold threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # displaying the video
    cv2.imshow("Live", gray)

    gray3=pytesseract.image_to_string(gray)
    # exiting the loop
    key=cv2.waitKey(1)
    if key == ord("q"):
        break
print(gray3)
tr = Translator()
a = tr.translate(gray3, src= 'en', dest='ur')
b=a.text
print(b)
engine.say(gray3)
engine.runAndWait()
engine.stop()
tts=gTTS(text=b,lang='ur',slow=False)
tts.save('ot.mp3')
os.system('ot.mp3')
source.release()
cv2.destroyAllWindows()
