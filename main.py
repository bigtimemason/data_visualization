import matplotlib.pyplot as plt
import numpy as np


year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.scatter(year, pop)

# formatting the plot
plt.title('Population (Billions) vs Year')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')

plt.show()