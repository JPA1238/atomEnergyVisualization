from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import random

import json

with open('IsotopicMass.json', 'r') as f:
    isotopicMass = json.loads(f.read())

xpos = []
ypos = []
zpos = []

for element in isotopicMass :
    element = element.replace('element', '')
    element = element.split('.')
    xpos.append(element[0])
    ypos.append(element[1])
    zpos.append(0)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

num_elements = len(xpos)
dx = np.ones(len(xpos))
dy = np.ones(len(ypos))
dz = []
for i in range(len(xpos)):
    dz.append(random.randint(0, 20))

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()