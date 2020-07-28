import cv2
import numpy as np


def add_num(img_path, text):
    img = cv2.imread(img_path)
    edited_img = cv2.putText(img, '0000', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.imshow('edited_img', edited_img)
    cv2.waitKey(0)

if __name__ == "__main__":
    add_num('./0000/test.jpg', '0000')
    pass   
