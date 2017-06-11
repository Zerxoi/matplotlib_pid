__author__ = 'Zerxoi'
import matplotlib.pyplot as plt
import numpy as np


class PID:
    def __init__(self, kp, ki, kd, sample_time=0.01):  # default sample time : 10ms
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.sample_time = sample_time
        self.first_flag = True
        self.last_error = 0
        self.feedback = 0
        self.integral = 0
        self.output = 0

    def update(self, set_point):
        """pid update method"""

        error = set_point - self.feedback

        if self.first_flag:
            '''first time have no integral item and derivative item'''
            derivative = 0
            '''first time complete'''
            self.first_flag = False
        else:
            self.integral += error
            derivative = (error - self.last_error)

        self.output = self.kp * error + self.ki * self.integral + self.kd * derivative

        '''update attribute'''
        self.last_error = error
        self.feedback = self.output

        return self.output

kp = 0.4
ki = 0.8
kd = 0.05

x = []
y11 = [0]
y12 = [0]
y21 = [0]
y22 = [0]

pid1 = PID(kp, ki, kd)  # default sample time : 10ms
pid2 = PID(kp, ki, kd)  # default sample time : 10ms

for point_num in range(200):
    t = point_num * pid1.sample_time
    set_line = 50
    output_line = pid1.update(set_line)
    set_curve = 10 * np.sin(2*np.pi*t)
    output_curve = pid2.update(set_curve)
    x.append(t)
    y11.append(set_line)
    y12.append(output_line)
    y21.append(set_curve)
    y22.append(output_curve)

y11.pop()
y12.pop()
y21.pop()
y22.pop()

plt.subplot(121)
plt.plot(x, y11, 'b--', x, y12, 'r')
plt.title('Line')

plt.subplot(122)
plt.plot(x, y21, 'b--', x, y22, 'r')
max_difference_y = max(y21) - min(y21)
plt.ylim(min(y21)-0.1*max_difference_y, max(y21)+0.1*max_difference_y)
plt.title('Curve')

plt.grid()
plt.show()
