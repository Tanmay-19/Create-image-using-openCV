import cv2
import numpy
a= numpy.zeros((500,500,3))
a[0:]=[0,0,255]
a[100:121,50:331]=[255,255,255]
a[100:401,50:71]=[255,255,255]
a[100:121,350:451]=[255,255,255]
a[401:421,50:401]=[255,255,255]
a[60:161,390:411]=[255,255,255]
a[180:421,390:411]=[255,255,255]
a[345:371,170:291]=[255,255,255]
a[170:351,217:248]=[255,255,255]
a[170:195,175:246]=[255,255,255]
cv2.imshow('Oneplus Logo', a)
cv2.waitKey()
cv2.destroyAllWindows()
