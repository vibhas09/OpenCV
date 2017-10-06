import cv2
cameraCapture = cv2.VideoCapture(0)
fps = 30 # an assumption
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('MyOutputVid.avi',fourcc, fps, size)
success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.imshow('new',frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1
cameraCapture.release()
cv2.destroyAllWindows()
