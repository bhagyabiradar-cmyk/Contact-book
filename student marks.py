import matplotlib.pyplot as plt

subjects = ["Python", "Maths", "English", "SQL", "AI"]
marks = [85, 78, 90, 82, 88]

plt.bar(subjects, marks)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()