# Text Detection using OCR

## Video text detection:
The script uses OpenCV methods :

- cv.threshold() :is used to apply the thresholding.
- findContours() :finds the contours, a useful tool for shape analysis and object detection and recognition.
- cv2.rectangle(): To draw a rectangle over the detected text. 
- cv2.GaussianBlur(): To blur the shape.


This is the 3 stages of a frame : original->detected text with a box -> blurred text :
![example over a frame:](https://github.com/DataloopTraining/OCR-snippets/blob/main/textdetection/combine_images.jpg)










