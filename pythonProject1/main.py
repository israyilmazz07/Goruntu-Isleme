import cv2
import numpy as np
kus=cv2.imread("kus.jpg",0)
cv2.imshow("kus.jpg",kus)
cv2.waitKey()


stringboyut=256
stringAralık=(0,256)

Hist = np.zeros(256)
k,l =kus.shape

for u in range(0,k):
    for v in range(0,l):
        deger = kus[u,v]
        Hist[deger]= deger +1



