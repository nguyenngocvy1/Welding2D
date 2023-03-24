# import matplotlib.pyplot as plt
# fig = plt.figure(1)	#identifies the figure 
# plt.title("Y vs X", fontsize='16')	#title
# plt.plot([1, 2, 3, 4], [6,2,8,4])	#plot the points
# plt.xlabel("X",fontsize='13')	#adds a label in the x axis
# plt.ylabel("Y",fontsize='13')	#adds a label in the y axis
# plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot
# plt.savefig('Y_X.png')	#saves the figure in the present directory
# plt.grid()	#shows a grid under the plot
# plt.show()


from math import *
import json
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animation_frame(i):
    t1 = theta1[i]
    t2 = theta2[i]
    x1 = x0 + l1*cos(t1)
    y1 = y0 + l1*sin(t1)
    x2 = x1 + l2*cos(t2)
    y2 = y1 + l2*sin(t2)
    line1.set_xdata([x0,x1])
    line1.set_ydata([y0,y1])
    line2.set_xdata([x1,x2])
    line2.set_ydata([y1,y2])
    x.append(x2)
    y.append(y2)
    return line1, line2,

#========================= SCARA ROBOT CONFIGURATION =========================
data = {'theta1':[],'theta2':[],'x':[],'y':[]}
x0 = 0
y0 = 0
l1 = 1 #m for first robotic arm
l2 = 0.5 #m for second robotic arm
n_theta = 1 #no of division for simulation
theta_start = 0
theta_end = 360
theta1 = []
theta2 = []
x = []
y = []

#===================== DRAW =================================
fig, ax = plt.subplots()
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
line1, = ax.plot([],[])
line2, = ax.plot([],[])

#======================= INPUT DATA ================================
# x, y = 0,0
# q2 = acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))
# q1 = atan(y/x) - atan((l2*sin(q2))/(l1 + l2*cos(q2)))

for i in range(theta_start,theta_end+1,n_theta):
    for j in range(theta_start,theta_end+1,n_theta):
        q1 = radians(i)
        q2 = radians(j)
        theta1.append(q1)
        theta2.append(q2)

anime = FuncAnimation(fig,func=animation_frame, interval=1)
data['theta1'] = theta1
data['theta2'] = theta2
data['x'] = x
data['y'] = y
with open('output.json', 'w') as outfile:
    json.dump(data, outfile)
plt.show()
