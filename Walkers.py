import cv2


# Create our body classifier
body_detect =  cv2.CascadeClassifier("haarcascade_fullbody.xml")

# Initiate video capture for video file
video = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = video.read()

    #Convert Each Frame into Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    body = body_detect.detectMultiScale(gray)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in body :
        cv2.rectangle(frame , (x,y), (x+w, y+h), (000, 000, 255), 2)

    cv2.imshow("output", frame)

    if cv2.waitKey(20) == 32: #32 is the Space Key
        break

video.release()
cv2.destroyAllWindows()
