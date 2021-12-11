import matplotlib.pyplot as plt
import math
h = 356
k = 380
samp = 0.001
loop = math.radians(0)
x = -k * math.cos(math.radians(65) - 0.3) + h * math.cos(-0.3)
y = -k * math.sin(math.radians(65) - 0.3) + h * math.sin(-0.3)
print("TAN2 CHECK: ",math.degrees(math.atan2(-0.3,1)))
fig,axes = plt.subplots(3)
axes[0].set_xlim([-100, 100])
axes[0].set_ylim([-200, -600])
axes[0].set_title("X and Y coordinates of the leg")
axes[1].set_title("Theta 1")
axes[2].set_title("Theta 2")
j=0
while(loop<math.radians(90)):
    x = x-samp*50
    y = y-(0.1*math.sin(loop))
    print("X,Y: ",x,y)
    th2 = math.acos((math.pow(k, 2) + math.pow(h, 2) - math.pow(x, 2) - math.pow(y, 2)) / (2 * k * h))
    print("theta2: ",math.degrees(th2))
    a = -k*math.cos(th2)+h
    b = k*math.sin(th2)
    th1 = math.atan2(b,a) + math.atan2(y,x)
    print("theta1: ",math.degrees(th1))
    loop+=0.001
    axes[0].scatter(x,y)
    axes[1].scatter(j,math.degrees(th1))
    axes[2].scatter(j,math.degrees(th2)-65)
    j = j+0.001
loop = math.radians(90)
samp = 0.001
while(loop<math.radians(180)):
    x = x-samp*50
    y = y+(0.1*math.sin(loop))
    print("X,Y: ",x,y)
    th2 = math.acos((math.pow(k, 2) + math.pow(h, 2) - math.pow(x, 2) - math.pow(y, 2)) / (2 * k * h))
    print("theta2: ",math.degrees(th2))
    a = -k * math.cos(th2) + h
    b = k * math.sin(th2)
    th1 = math.atan2(b,a) + math.atan2(y,x)
    print("theta1: ", math.degrees(th1))
    loop+=0.001
    axes[0].scatter(x, y)
    axes[1].scatter(j, math.degrees(th1))
    axes[2].scatter(j, math.degrees(th2)-65)
    j=j+0.001
plt.show()