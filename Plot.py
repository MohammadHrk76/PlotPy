import numpy as np
import matplotlib.pyplot as plt
####################################
x = np.array([0,7])
y = np.array([0,400])

plt.plot(x,y)

plt.subplot(2, 3, 1)
#######################################

y = np.array([36, 150, 230, 286 , 300])

plt.plot(y, marker = 'o', color = "purple", ms = 5, mec = "r", mfc = "r")

plt.subplot(2, 3 , 2)

#######################################

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.grid()

plt.plot(x, y)
plt.subplot(2, 3 , 3)

#######################################

x = np.array(["A", "B", "C", "D"])
y = np.array([2, 7, 6, 10])

plt.bar(x,y, color = "green")

plt.subplot(2, 3 , 3)

#######################################

x = np.random.normal(170, 10, 250)

plt.subplot(2, 3 , 4)

plt.hist(x, color = "blue")

#######################################

y = np.array([35, 25, 25, 15])

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.subplot(2, 3 , 5)

plt.pie(y, labels = mylabels)

plt.legend(title = "Four Fruits:")

#######################################

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.subplot(2, 3 , 6)

plt.scatter(x, y)
#####################################
plt.show()
