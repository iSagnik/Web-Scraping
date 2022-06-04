import numpy as np
import cv2
from sewar.full_ref import uqi
import imagehash
from PIL import Image
import sys
# img = cv2.imread('images/sample/jpg_2.jpg')
# #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# down_width = 300
# down_height = 200
# down_points = (down_width, down_height)
# resized_down = cv2.resize(img, down_points, interpolation= cv2.INTER_LINEAR)

# up_width = 800
# up_height = 600
# up_points = (up_width, up_height)
# resized_up = cv2.resize(img, up_points, interpolation= cv2.INTER_LINEAR)

# cv2.imshow('RedBull', img)
# cv2.imshow('Resized Down ', resized_down)
# cv2.waitKey(0)
# cv2.imshow('Resized Up image ', resized_up)
# cv2.waitKey()
# #cv2.imshow('images/, gray)

classes = ['cats', 'dogs', 'cars']

for cls in classes:
    cv2.imsave(f'images/{cls}/jpg_0.jpg')

# cv2.destroyAllWindows()

# #cv2.imwrite('./images/cat/newgreyone2.jpg', gray)

user_query = input("Enter class name: ")
MAX_COUNT = int(input("Enter the number of images"))
web_scraped = []

while MAX_COUNT > 0:
    if img1 == img2:
        MAX_COUNT = MAX_COUNT - 1
        cv2.imsave(f'images/{user_query}/jpg_{MAX_COUNT}.jpg')




cat1 = cv2.imread("images/cat/jpg_0.jpg")
cat2 = cv2.imread("images/cat/jpg_1.jpg")

# cat1_hash = imagehash.average_hash(Image.open("images/cat/jpg_4.jpg"))
# cat2_hash = imagehash.average_hash(Image.open("images/cat/jpg_5.jpg"))

# if cat1_hash - cat2_hash > 5:
#     print("images are similar")
# else:
#     print ("images are not similar")

cv2.imshow('Cat', cat1)
cv2.destroyAllWindows()

cat1 = cv2.resize(cat1, (300, 200), interpolation=cv2.INTER_LINEAR)
cat2 = cv2.resize(cat2, (300, 200), interpolation=cv2.INTER_LINEAR)

print (uqi(cat1,cat2))




