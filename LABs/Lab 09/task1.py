import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
students = [f'Student {i+1}' for i in range(20)]
heights = np.random.randint(150, 200, size=20)  

plt.figure(figsize=(15, 6))


plt.subplot(1, 2, 1) 
bar_colors = plt.cm.magma(np.linspace(0, 1, len(students)))  
plt.bar(students, heights, color=bar_colors)
plt.title('Student Heights Bar Chart')
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.subplot(1, 2, 2)  
plt.pie(heights, labels=students, autopct='%1.1f%%', startangle=140, colors=bar_colors, textprops={'color': 'white'})
plt.title('Student Heights Pie Chart')
plt.axis('equal')  

plt.tight_layout()
plt.show()
