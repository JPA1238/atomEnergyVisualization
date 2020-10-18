from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import random

import json

massElectron = 0.00054858
massProton = 1.0072765
massNeutron = 1.0086649
uTOKgConversion = 1.67258*pow(10, -27)
lightSpeed2 = 89875517873681764
JTOMeVConversion = 1.6021773 * pow(10, -19)

with open('IsotopicMass.json', 'r') as f:
    isotopicMass = json.loads(f.read())

xpos = []
ypos = []
zpos = []
dz = []

for element in isotopicMass :
    elementName = element
    element = element.replace('element', '')
    element = element.split('.')
    element = np.array(element).astype(np.float)
    print(element, type(element[0]))
    xpos.append(element[0])
    ypos.append(element[1] - element[0])
    zpos.append(0)
    
    molarMassCoreWithoutBounds = (element[0] * massProton) + ((element[1] - element[0]) * massNeutron)
    molarMassCore = isotopicMass[elementName]['AtomicMass'] - (element[0] * massElectron)
    lostMass = molarMassCoreWithoutBounds - molarMassCore
    bindingEnergy = lostMass * 931.48
    specificBindingEnergy = bindingEnergy / element[1]
    print(specificBindingEnergy)
    '''
    lostMass *= uTOKgConversion
    bindingEnergy = lostMass * lightSpeed2
    bindingEnergy *= JTOMeVConversion
    specificBindingEnergy = bindingEnergy / element[1]
    '''
    '''
    molarMassCore = isotopicMass[elementName]['AtomicMass'] - (element[0] * massElectron)
    if isotopicMass[elementName]['AtomicMass'] == -1:
      molarMassCore = 0
    print(elementName, molarMassCore)
    massCore = molarMassCore * uTOKgConversion
    restEnergyCore = massCore * lightSpeed * lightSpeed
    '''
    if isotopicMass[elementName]['AtomicMass'] != -1:
        dz.append(specificBindingEnergy)
    else:
        dz.append(0)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

num_elements = len(xpos)
dx = np.ones(len(xpos))
dy = np.ones(len(ypos))

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()
