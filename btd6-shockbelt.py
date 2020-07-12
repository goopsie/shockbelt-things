import pytesseract
import pyautogui
import cv2
import numpy as np
import os
from PIL import ImageGrab, Image

shockcmd = "curl \"https://api.particle.io/v1/devices/.../shock\" -H \"Authorization: Bearer ...\" --data-raw \"arg=3\"" # bad person browsing my github repo, bad
lastknownlives = 100



def main():
    global lastknownlives
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    while(True):
        img = getImage()
        cv2.imshow('image',img)
        try:
            currentlives = int(pytesseract.image_to_string(img, lang='eng', config='--psm 7 -c tessedit_char_whitelist=0123456789')) # char_whitelist is very nice and cool
            print(currentlives)
            if currentlives = 4: # i don't care about ignoring 4, sometimes it thinks 40 is 4
                continue
            if currentlives > lastknownlives:
                lastknownlives = currentlives
                continue
            if currentlives < lastknownlives:
                shock()
                lastknownlives = currentlives
        except ValueError: # image doesn't contain anything that can be converted into int
            print("Nothing found in image")
        
        if cv2.waitKey(25) & 0xFF == ord('x'):  
            cv2.destroyAllWindows()
            break




def getImage():
    _, img = cv2.threshold(np.array(ImageGrab.grab(bbox=(116, 23, 196, 61)).convert('L')),254,255,cv2.THRESH_BINARY_INV)
    return img

def shock():
    print("Oopsie Woopsie!!! You fucked up!!!")
    os.system(shockcmd) # i don't careeee
    return True

if __name__ == "__main__":
    main()
        




