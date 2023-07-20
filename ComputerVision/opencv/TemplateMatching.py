import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# img = cv.imread("D:/PracticeAll/Images/testingimg.jpg")
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# template = cv.imread('D:/PracticeAll/Images/testingimg2.jpg',0)
# w, h = template.shape[::-1]

# res = cv.matchTemplate(gray_img, template, cv.TM_CCORR_NORMED)
# print(res)
# threshold = 0.99;
# loc = np.where(res >= threshold)
# print(loc)
# for pt in zip(*loc[::-1]):
#     cv.rectangle(img, pt, (pt[0] + w, pt[1]+ h), (0, 0, 255), 2)

# cv.imshow("Template",template)
# cv.imshow("IMG", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

###################### Multiple Template Matching###############################

img = cv.imread("D:/PracticeAll/Images/mario4.jpeg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

template = cv.imread("D:/PracticeAll/Images/mario4temp1.jpeg",0)
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray,template, cv.TM_CCOEFF_NORMED)
print(res)
threshold = 0.88;
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,0,255),2)
   

cv.imshow('template',template)
cv.imshow("IMG", img)
cv.waitKey(0)
cv.destroyAllWindows()
