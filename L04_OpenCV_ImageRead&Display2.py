import cv2 as cv 
import sys 

img = cv.imread('soccer.jpg')

# Image Display라는 창에 img띄우고, (0,0)의 B, G, R값 출력
cv.imshow('Image Display', img) 
print(img[0,0,0], img[0,0,1], img[0,0,2])

cv.waitKey()
cv.destroyAllWindows()
