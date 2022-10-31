import cv2
import numpy as np

kus=cv2.imread("kus.jpg",0)
cv2.imshow("kus.jpg",kus)
cv2.waitKey()
max= (np.max(kus) - np.min(kus))/(np.max(kus) + np.min(kus)) # maxımum değeri bulur.

[l,m] = kus.shape
new_kus = np.zeros([l,m], dtype=np.uint8)
for i in range(l):
    for j in range(m):
        new_kus[i,j] = max - kus[i,j]  #maxımum değerden görüntüyü çıkartıp görüntünün ters görünmesini sağlıyo.


cv2.imshow("Manuel_inverted",new_kus)
cv2.waitKey()