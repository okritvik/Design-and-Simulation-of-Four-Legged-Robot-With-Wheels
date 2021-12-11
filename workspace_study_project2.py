import matplotlib.pyplot as plt
import math
h = 356
k = 380
th1 = math.radians(0)
fig = plt.figure()
while(th1>=math.radians(-90)):
    th2 = math.radians(90)
    while(th2>=math.radians(30)):
        # x = -(k * math.cos(math.radians(th2))) + (h * math.cos(th1))
        x = h*math.cos(th1)-k*math.cos(th2)
        y = h*math.sin(th1)-k*math.sin(th2)
        print(math.cos(th1))
        # y = -(k * math.sin(math.radians(th2))) + (h * math.sin(th1))
        print("x,y: ",x,y,math.degrees(th1),math.degrees(th2))
        plt.scatter(x,y)
        th2 = th2 - math.radians(1)
    th1 = th1 - math.radians(3)
plt.show()
