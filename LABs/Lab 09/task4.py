import matplotlib.pyplot as plt
import numpy as np

student_ages = [18, 22, 19, 25, 26, 30, 31, 34, 29, 27, 22, 36, 40, 41, 20, 24, 23, 35, 38, 45]
age_groups = ['18-25', '26-30', '31-35', '36 and above']

age_distribution = [
    sum(1 for age in student_ages if 18 <= age <= 25),
    sum(1 for age in student_ages if 26 <= age <= 30),
    sum(1 for age in student_ages if 31 <= age <= 35),
    sum(1 for age in student_ages if age >= 36)
]

color = plt.cm.twilight(np.linspace(0,1, len(student_ages)))

plt.pie(age_distribution, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=color)
plt.title("Age Distribution Chart")
plt.axis("equal")
plt.show()
