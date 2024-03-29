import matplotlib.pyplot as plt
import numpy as np

import json

massElectron = 0.00054858
massProton = 1.0072765
massNeutron = 1.0086649
uTOKgConversion = 1.660540199e-27
lightSpeed = 299792458
JTOMeVConversion = 6241506479963.2
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
    xpos.append(element[0])
    ypos.append(element[1] - element[0])
    zpos.append(930)

    molarMassCore = isotopicMass[elementName]['AtomicMass'] - (element[0] * massElectron)
    if isotopicMass[elementName]['AtomicMass'] == -1:
      molarMassCore = 0
    massCore = molarMassCore * uTOKgConversion
    restEnergyCore = massCore * lightSpeed**2
    restEnergyCore = restEnergyCore * JTOMeVConversion
    specificRestEnergyCore = restEnergyCore / element[1]
    print(specificRestEnergyCore)
    if isotopicMass[elementName]['AtomicMass'] != -1:
        dz.append(specificRestEnergyCore - 930)
    else:
        dz.append(0)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

num_elements = len(xpos)
dx = np.ones(len(xpos))
dy = np.ones(len(ypos))

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()
