from PIL import Image
import pytesseract
import requests 
import re
import uuid
import cv2
import numpy as np
import os
for i in range(100):
    content = requests.get('https://ipindiaonline.gov.in/eregister/captcha.ashx').content
    captcha_path = 'public/' + uuid.uuid4().hex + '.jpeg'
    with open(captcha_path, 'wb') as f:
        f.write(content)
        f.close()

    image = Image.open(captcha_path)
    #gray = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #gray = cv2.cvtColor(cv2.UMat(np.float32(image)), cv2.COLOR_RGB2GRAY)

    #gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #gray = cv2.medianBlur(gray, 3)

    dpi_path = captcha_path.replace('.jpeg', '_600.jpeg')
    image.save(dpi_path, dpi=(600,600))

    text = pytesseract.image_to_string(Image.open(dpi_path))
    if re.findall('\d+',text):
        print(dpi_path)
        print(text)
    os.remove(captcha_path)
