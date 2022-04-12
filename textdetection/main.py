import cv2
import os

# Read image from which text needs to be extracted
video_path = "last.mp4"

if not os.path.isfile(video_path):
    raise ValueError('file not exists: {}'.format(video_path))
out_video_path = video_path + '_out.mp4'
# read input video
reader = cv2.VideoCapture(video_path)
width = int(reader.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(reader.get(cv2.CAP_PROP_FPS))
encoding = int(reader.get(cv2.CAP_PROP_FOURCC))
n_frames = int(reader.get(cv2.CAP_PROP_FRAME_COUNT))
writer = cv2.VideoWriter(
    out_video_path,
    cv2.VideoWriter_fourcc(*'MP4V'), fps, (width, height))

i_frame = 0
while reader.isOpened():
    ret, frame = reader.read()
    if not ret:
        break
    ret, frame = reader.read()
    # Convert the image to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    # Creating a copy of image to be the output
    frame2 = frame.copy()
    # Looping through the identified contours
    # drawing boxes over the text and then showing the new img
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # Drawing a rectangle on copied image
        if  frame2.shape[0] * 0.5 > h and  frame2.shape[1] * 0.5 > w:
            rect = cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # write
        writer.write(frame2)
        i_frame += 1

reader.release()
writer.release()
