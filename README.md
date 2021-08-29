# Number-plate-localzation

This is a simple algorrithm to localozre the vehicles number plate suing OpenCV-python library. 

First we import the image and using the imutils library we have  resized the image. Using the cv2 metrhod we have removed the RGB and convereted ton grascale and processed the image
for noise reduction. Using the canny edge detector we have created all the existing contours of the images.

![canny edge](https://user-images.githubusercontent.com/61246422/131240070-f24d0e77-315d-48c1-9aba-b3f80d14e789.JPG)

Then using the findcontours method all the countours are drawn with green bounding boxes and the sorted based on contour area and then top 45 countours are selected. 
And only that contour is selected whcih contains 4 definite edges which is cropped at first from the image and the bounding box is created withon that contour with 4 edges which is our license plate in this case. 

![crop license](https://user-images.githubusercontent.com/61246422/131240167-b9747ca1-44ae-4dae-91c8-d1bf5b3b9a99.JPG)

![deetcted](https://user-images.githubusercontent.com/61246422/131240172-3226a87a-c62f-4bc5-9af6-1d62fbff8154.JPG)



