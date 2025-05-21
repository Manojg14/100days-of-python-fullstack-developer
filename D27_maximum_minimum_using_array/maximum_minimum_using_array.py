
# maximum and minimum element of an array

from array import *

data = array('i',[1,0,32,4,5,10])

max_value = data[0]
min_value = data[0]

for i in range (1,len(data)):
    if data[i] > max_value:
        max_value = data[i]
    if data[i] < min_value:
        min_value = data[i]

print(f"maximum element is {max_value}")
print(f"minimum element is {min_value}")