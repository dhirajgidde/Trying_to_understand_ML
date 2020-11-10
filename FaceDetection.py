import cv2




classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


img = cv2.imread('2.jpg')
#img1 = cv2.imread('D:\\b1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

faces = classifier.detectMultiScale(gray)
#print("number of Faces Detedcted:", faces.shape[0])

for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 2)
   # img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
#cv2.imshow('img1', img1)

'''if img[1]==img1[1]:
    print("they both are equal")
else:
    print("they are unequal")'''
cv2.waitKey(0)
cv2.destroyAllWindows()