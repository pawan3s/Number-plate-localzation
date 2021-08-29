import numpy as np
import cv2
import imutils

# Read Image
img = cv2.imread("images/car3.jpg")

# Image resize
image = imutils.resize(img, width=500)

# image to gray 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise Reduction 
filtered = cv2.bilateralFilter(gray, 11, 20, 20)

# Edge detction
canny_image = cv2.Canny(filtered, 50, 200)

# Finding contours
contours, new = cv2.findContours(canny_image.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )

# draw all contours on original image
img1 = image.copy()
cv2.drawContours(img1, contours, -1, (0, 0, 255), 1)

# Sort contours based on area
contours1 = sorted(contours, key=cv2.contourArea, reverse=True)[:45]
licensePlate = None

# only top 30 
img2 = image.copy()
cv2.drawContours(img2, contours1, -1, (0, 255, 0), 1 )


count = 0
idx =1
for c in contours1:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # print ("approx = ",approx)
        if len(approx) == 4:  # Select the contour with 4 corners
            NumberPlateCnt = approx #This is our approx Number Plate Contour

            # Crop those contours and store it in Cropped Images folder
            x, y, w, h = cv2.boundingRect(c) #This will find out co-ord for plate
            new_img = gray[y:y + h, x:x + w] #Create new image
            cv2.imwrite('cropped/' + str(idx) + '.png', new_img) #Store new image
            idx+=1

            break
cv2.imshow('icense Plate', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 2)
cv2.imshow("Final Image With Number Plate Detected", image)
cv2.waitKey(0)

# # Display Image
# # Hori = np.concatenate((image, img2), axis=1)
# cv2.imshow('icense Plate', Hori)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
