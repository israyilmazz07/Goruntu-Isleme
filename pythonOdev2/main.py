import cv2
import numpy as np

kus=cv2.imread("kus.jpg",0)
cv2.imshow("kus.jpg",kus)
cv2.waitKey()

max = np.max(kus)
print(max)

[l,m] = kus.shape
newkus = np.zeros([l,m], dtype=np.uint8)

for i in range(l):
    for j in range(m):
        newkus[i,j] = max - kus[i,j]  #maxımum değerden görüntüyü çıkartıp görüntünün ters görünmesini sağlıyo.


cv2.imshow("Negatif Kus",newkus)
cv2.waitKey()