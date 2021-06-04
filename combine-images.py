import cv2
import numpy

photo=cv2.imread("male.jpg")
photo.shape

cm=photo[:,:501]

cv2.imshow("Male",cm)
cv2.waitKey()
cv2.destroyAllWindows()

photo1=cv2.imread("female.jpg")
cf=photo1[:,501:]
cv2.imshow("Female",cf)
cv2.waitKey()
cv2.destroyAllWindows()

c= numpy.append(cm,cf,axis=1)

cv2.imshow("Collab",c)
cv2.waitKey()
cv2.destroyAllWindows()
