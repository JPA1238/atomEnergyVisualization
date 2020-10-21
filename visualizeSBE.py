import numpy as np
import matplotlib.pyplot as plt

import json

massElectron = 0.00054858
massProton = 1.0072765
massNeutron = 1.0086649
uTOKgConversion = 1.660540199e-27
lightSpeed = 299792458
JTOMeVConversion = 6241506479963.2
with open('IsotopicMass.json', 'r') as f:
    isotopicMass = json.loads(f.read())

xval = []
yval = []

for element in isotopicMass :
    elementName = element
    element = element.replace('element', '')
    element = element.split('.')
    element = np.array(element).astype(np.float)
    xval.append(element[1])
    massCoreWithoutBounds = element[0] * massProton + (element[1] - element[0]) * massNeutron
    massCore = isotopicMass[elementName]['AtomicMass'] - element[0] * massElectron
    massDefect = massCoreWithoutBounds - massCore 
    BE = massDefect * uTOKgConversion * lightSpeed**2
    BE = BE * JTOMeVConversion
    SBE = BE / element[1]

    if isotopicMass[elementName]['AtomicMass'] != -1:
        yval.append(SBE)
    else:
        yval.append(0)

plt.scatter(xval, yval)
#plt.plot(xval, yval)
plt.title('SBE')
plt.xlabel('A')
plt.ylabel('SBE (in MeV)')
plt.axhline(0, lw=0.5, color='black')
plt.axvline(0, lw=0.5, color='black')
plt.legend()
plt.show()
print('Done')