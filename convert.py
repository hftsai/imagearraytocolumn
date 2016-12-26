import numpy as np
import csv
a = np.loadtxt('IMG_0688-1.txt')
x=1
y=1
xend=a.shape[1]
with open('test.csv', 'wb') as csvfile:
    writer=csv.writer(csvfile, delimiter=',')
    writer.writerow(['x','y','data'])
    for element in a.flat:
        writer.writerow([x,y,element])
        x+=1
        if x >xend:
            x=1
            y+=1
