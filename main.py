'''Playing around with some data techniques. This repository is not named correctly.'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

data_frame1 = pd.read_excel('Book2.xlsx')

mass = []
msmr = []
lfespn = []

for num in data_frame1['Mass (kg)']:
    num = math.log(num)
    mass.append(num)
for num in data_frame1['MSMR (ml O2 g^-1 hr^-1)']:
    msmr.append(num)
for num in data_frame1['Approx. Lifespan (yr)']:
    num = math.log(num)
    lfespn.append(num)

plt.scatter(mass, lfespn)
z = np.polyfit(mass, lfespn, 1)
p = np.poly1d(z)

plt.plot(mass, p(mass), color="purple", linewidth=1, linestyle="--")

# formatting the plot
plt.title('Mass')
plt.xlabel('Mass (kg)')
plt.ylabel('Lifespan (years)')

plt.show()
