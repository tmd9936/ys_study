import numpy as np
import cv2
import math
import time


class Planet():
    """
    planet 
    """
    def __init__(self, speed, distance, color, thick=1):
        self.speed = speed
        self.distance = distance
        self.i = 0
        self.theta = 2.0 * 3.141592 * self.i / 360.0
        self.x = int(self.distance * math.cos(self.theta))
        self.y = int(self.distance * math.sin(self.theta))
        self.color = color
        self.thick = thick

    def update(self):
        self.i += self.speed
        if self.i >= 361:
            self.i = 0
        
        self.theta = 2.0 * 3.141592 * self.i / 360.0
        self.x = int(self.distance * math.cos(self.theta))
        self.y = int(self.distance * math.sin(self.theta))

p1 = Planet(1, 80, (10,153,210), -1)
p2 = Planet(0.4, 160, (200,13,90))

p_list = [p1,p2]

while True:
    img = np.ones((500,800,3), dtype=np.uint8) * 255
    
    cv2.circle(img, (360, 230), 30, (10,255,255), -1, lineType=cv2.LINE_AA)

    for i in range(len(p_list)):
        cv2.circle(img, (p_list[i].x+350, p_list[i].y+220), 5, p_list[i].color, p_list[i].thick, lineType=cv2.LINE_AA)
        p_list[i].update()
    
    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()

    