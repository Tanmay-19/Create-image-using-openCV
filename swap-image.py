import cv2

photo=cv2.imread('male.jpg')

cv2.imshow("Male Pic",photo)
cv2.waitKey()
cv2.destroyAllWindows()

cm=photo[120:480, 370:630]

cv2.imshow("Male Crop",cm)
cv2.waitKey()
cv2.destroyAllWindows()

photo1=cv2.imread('female.jpg')

cv2.imshow("Female pic",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cf=photo1[120:480,370:630]
cv2.imshow("Female Crop",cf)
cv2.waitKey()
cv2.destroyAllWindows()

photo[120:480, 370:630]=photo1[120:480,370:630]
cv2.imshow("Swap",photo)
cv2.waitKey()
cv2.destroyAllWindows()
