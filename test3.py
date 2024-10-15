import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [4,5,5,7])
left, right = plt.xlim(2,7)
print(left)
print(right)

plt.show()