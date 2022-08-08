import numpy as np
x = np.array([1,1,1])
y = np.array([0,0,0])
x+y
print(x+y)
-------
np.add(x,y)
x.dtype
x.shape
x.size
x.ndim


import numpy as np
w = np.array([[12,14,16],[11,13,15]])
print(w)

import numpy as np
z =np.arange(1, 4)
print(z)
Array=np.vstack((z, w))
newArray = Array.copy()
newArray

for item in newArray.flat:
    print(item)
    newArray.transpose()

    newArray -= 1
newArray
newArray.min()
newArray.max()
newArray[0]
newArray[1, 1]
newArray[0,1:2] 
ewArray[2,2:3] 
newArray

newArray = newArray.reshape(9,1)
newArray
newArray 
newArray = newArray.reshape(3,2)
newArray