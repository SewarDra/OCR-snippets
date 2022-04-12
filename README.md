# Text Detection using OCR

## Video text detection:
The script uses OpenCV methods :

- cv.threshold() :is used to apply the thresholding.
- findContours() :finds the contours, a useful tool for shape analysis and object detection and recognition.
- cv2.rectangle(): To draw a rectangle over the detected text. 
- cv2.GaussianBlur(): To blur the shape.

> note that the output video in the file is not blurred,if you want you can uncomment the blur lines in the script.

![example over a frame:](https://github.com/DataloopTraining/OCR-snippets/blob/main/textdetection/combine_images.jpg)










