import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6]

plt.plot(x,np.power(x,2),'k^:',x,np.power(x,3),'c+:')

plt.xlabel("X asix")
plt.ylabel("Y asix")

plt.title("First PLot")

plt.show()