import cv2
import numpy as np

image = cv2.imread("E:\FinalProject\Source Images\Source.jpg",1)
gray= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
gray_f=cv2.resize(gray,(1280,720))
cv2.imshow("Grayscale", gray_f)
image_resize=cv2.resize(image,(1280,720))
#cv2.imshow("OG",image_resize)
cv2.imwrite("E:\FinalProject\Product Images\Original.png", image_resize)

#Threshold
height,width = gray_f.shape[0:2]
blur=cv2.GaussianBlur(gray_f,(5,5),0)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(blur,cv2.MORPH_OPEN,kernel, iterations=2)
cv2.imwrite("E:\FinalProject\Product Images\Blur and Noise Removal.png",opening)
ret, thresh_adapt = cv2.threshold(opening, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#cv2.imshow("Binary",thresh_adapt)
cv2.imwrite("E:\FinalProject\Product Images\Binary Image.png",thresh_adapt)

#Contours
_,contours,hierarchy = cv2.findContours(thresh_adapt,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
low_thicc= image_resize.copy()
index=-1
thickness=2
color=(0,255,255)
cv2.drawContours(image_resize, contours, index, color, thickness)
cv2.imshow("Contours", image_resize)
cv2.imwrite("E:\FinalProject\Product Images\Output_2T.png", image_resize)
thicknessL = 1
cv2.drawContours(low_thicc,contours,index,color,thicknessL)
cv2.imwrite("E:\FinalProject\Product Images\Output_1T.png", low_thicc)
cv2.waitKey()
cv2.destroyAllWindows()
