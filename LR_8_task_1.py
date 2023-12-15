import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("volkov_full.jpg")
# DISPLAY
cv2.imshow("volkov", img)
cv2.waitKey(0)
