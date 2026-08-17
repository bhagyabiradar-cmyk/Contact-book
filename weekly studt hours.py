import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [2, 3, 2.5, 4, 3, 5, 4.5]

plt.plot(days, hours, marker="o")

plt.xlabel("Days")
plt.ylabel("Study Hours")
plt.title("Weekly Study Hours")

plt.show()