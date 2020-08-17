import cv2

img = cv2.imread('shapes.png')
cv2.imshow('original', img)
# video = cv2.VideoCapture(0)
# _, img = video.read()
# while video.isOpened():
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx] ,0, (0,0,0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx)== 3:
        cv2.putText(img, "TRIANGLE", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif len(approx)== 4:
        x,y,w,h = cv2.boundingRect(approx)
        if w == h :
            cv2.putText(img, "SQUARE" ,(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
        else:
            cv2.putText(img, "RECTANGLE" ,(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

    elif len(approx)== 5:
        cv2.putText(img, "PENTAGON" ,(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif len(approx)== 6:
        cv2.putText(img, "HEXAGON" ,(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif len(approx)== 7:
        cv2.putText(img, "HEPTAGON" ,(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif len(approx)== 8:
        cv2.putText(img, "OCTAGON" ,(x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    elif len(approx) == 10:
        cv2.putText(img, "STAR", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
    else:
        cv2.putText(img, "CIRCLE", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)


cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()