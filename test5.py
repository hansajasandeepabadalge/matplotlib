import matplotlib.pyplot as plt

age = [10, 45, 24, 54, 13, 64, 74, 78]
weight = [20, 60, 40, 49, 30, 100, 67, 80]  # Added an extra element to match the length of 'age'

plt.plot(age, weight)
plt.xlabel('Age')
plt.ylabel('Weight')
plt.title('Age vs Weight')

plt.show()