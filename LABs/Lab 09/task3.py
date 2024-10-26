import matplotlib.pyplot as plt
import numpy as np

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolate Chip', 'Crunch', 'Brownie', 
           'Cookies and Cream', 'Rocky Road', 'Pistachio', 'Mango', 'Coffee', 'Blueberry', 'Pineapple']
scoops_sold = [150, 200, 120, 80, 95, 151, 110, 170, 130, 200, 145, 168, 192]


plt.figure(figsize=(8, 8))
colors = plt.cm.coolwarm(np.linspace(0, 1, len(flavors))) 

plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'color': 'black'})  
plt.title("Distribution of Ice Cream Sales")
plt.axis('equal')  
plt.show()
