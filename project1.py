import cv2
vid = cv2.VideoCapture(0)
fd = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

frameCount =0
name = input('Enter Your Name:')
while True:
    flag, img = vid.read()
    if flag:
        faces = fd.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),1.1,5, minSize = (50,50))
        if len(faces)==1:
            x,y,w,h = faces[0]
            img_face = img[y:y+h, x:x+w, :].copy()
            cv2.imwrite(f'{name}_{frameCount}.png', img_face)
            frameCount +=1
            if frameCount==20:
                break
            cv2.imshow('Preview', img)
        key=cv2.waitKey(1)
        if key == ord('x'):
            break
vid.release()
cv2.destroyAllWindows()
cv2.waitKey(1)