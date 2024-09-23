"""
#Create a simple line plot using Matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5] 
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker='*' )
plt.title("Simple Line Plot")
plt.title("x-axis")
plt.title("y-axis")
plt.show()

#Create a bar chart to display sales data of three products.
# products = ['Television', 'Laptop', 'Mobile']sales = [150, 200, 300].
import matplotlib.pyplot as plt
products = ['Television', 'Laptop', 'Mobile']
sales = [150, 200, 300]

plt.bar(products, sales)
plt.title("bar chart of sales data of three products")
plt.xlabel("products")
plt.ylabel("sales")
plt.show()


#Task 3: Create a scatter plot with random data for x and y.
#Use x = [5, 7, 8, 7, 2] and y = [99, 86, 87, 88, 100].
import matplotlib.pyplot as plt
x = [5, 7, 8, 7, 2]
y = [99, 86, 87, 88, 100]
plt.scatter(x, y)
plt.title("Scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


#Task 4: Create a customized line plot with labels for axes and a title.
#Use x = [1, 2, 3, 4] and y = [10, 20, 25, 30] and add a title and labels for x-axis and y-axis.

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Line graph between X and Y")
plt.xlable("X-axis")
plt.ylable("Y-axis")
plt.show()




import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()




#Task 5: Create a bar chart with different colors for each bar.
#Use categories = ['A', 'B', 'C', 'D'] and values = [5, 7, 3, 8].
import matplotlib.pyplot as plt




import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
colors = ["purple", "black", "brown", "pink"]

plt.bar(categories, values, color =  colors)
plt.title("Bar Chart")
plt.xlabel("categories")
plt.ylabel("values")
plt.show()



#Task 6: Create a subplot with two charts:
#One line plot for x = [1, 2, 3, 4] and y = [10, 20, 25, 30].
#One bar chart for categories = ['A', 'B', 'C'] and values = [50, 70, 30]
import matplotlib.pyplot as plt

# Data for line plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Data for bar chart
categories = ['A', 'B', 'C']
values = [50, 70, 30]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(x, y, marker='+', color='blue')

ax1.set_title('Line Plot')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

ax2.bar(categories, values, color=['purple', 'pink', 'blue'])
ax2.set_title('Bar Chart')
ax2.set_xlabel('Categories')
ax2.set_ylabel('Values')

plt.tight_layout()

plt.show()




#Task 7: Create a pie chart to represent the percentage of students with grades A, B, C, and F.
#Use labels = ['A', 'B', 'C', 'F'] and sizes = [15, 30, 45, 10].
import matplotlib.pyplot as plt
lables = ['A', 'B', 'C', 'F']
sizes = [15, 30, 45, 10]

colors = ['blue', 'purple', 'pink', 'green']
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=lables, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title("Pie Chart of Students percentage")
plt.show()


#Task 8: Create a line plot and customize it with different colors, markers, and line styles.
#Use x = [1, 2, 3, 4] and y = [10, 20, 25, 30] with a red line, circular markers, and a dashed line style.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o', linestyle='dashed')
plt.title("line graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()




#Task 9: Create a bar chart and customize the width and alignment of the bars.
#Use categories = ['A', 'B', 'C', 'D'] and values = [5, 7, 3, 8].
import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, width=0.6, align='center', color='purple')
plt.title("Bar Chart")
plt.xlabel("categories")
plt.ylabel("values")
plt.show()



#Task 10: Create a figure with two subplots:
#One plot shows a scatter plot of x = [1, 2, 3, 4] and y = [10, 20, 25, 30].
#Another plot shows a pie chart for labels = ['A', 'B', 'C'] and sizes = [40, 30, 30].


import matplotlib.pyplot as plt
# Data for the scatter plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Data for the pie chart
labels = ['A', 'B', 'C']
sizes = [40, 30, 30]
colors = ['gold', 'yellowgreen', 'lightcoral']

# Create a figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Scatter plot on the first subplot
ax1.scatter(x, y, color='blue', marker='+')
ax1.set_title('Scatter Plot')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

# Pie chart on the second subplot
ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax2.set_title('Pie Chart')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()


# 4.2
#Task 1: Create a heatmap using Seaborn with the tips dataset.
#Use sns.heatmap(tips.corr(), annot=True).
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset

tips = load_dataset('tips')

tips = tips.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(8,6))
sns.heatmap(tips.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap of Tips Dataset")
plt.show()


#2 Create a pair plot using Seaborn with the tips dataset.
#Use sns.pairplot(tips).

import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import load_dataset

tips = sns.load_dataset('tips')
sns.pairplot(tips, hue='sex', palette='husl')
plt.title("Pair Plot")
plt.show()





#Task 3: Create a box plot of total_bill for each day using Seaborn.
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset

tips = load_dataset('tips')

plt.figure(figsize=(10, 10))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Box Plot')
plt.show()

"""

#Task 4: Create an interactive line plot using Plotly to show temperature trends over a week.
#Use days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] and temperature = [15, 16, 17, 19, 20, 18, 17].
"""

import plotly.express as px
import plotly.graph_objects as go

# Temperature trends over a week in Kathmandu
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperature = [15, 16, 17, 19, 20, 18, 17]

# Create a line plot using Plotly Express
fig = px.line(x=days, y=temperature, title='Temperature Trends in Kathmandu')

# Update axis labels
fig.update_layout(xaxis_title='Days', yaxis_title='Temperature (°C)')

# Show the plot
fig.show()
"""


"""
#Task 5: Create an interactive scatter plot using Plotly to visualize total_bill vs tip from the tips dataset.
import plotly.express as px
import seaborn as sns

# Load the 'tips' dataset from Seaborn
tips = sns.load_dataset('tips')

# Create a scatter plot using Plotly Express
fig = px.scatter(tips, x='total_bill', y='tip', 
                 title='Scatter Plot of Total Bill vs Tip',
                 labels={'total_bill': 'Total Bill ($)', 'tip': 'Tip ($)'}, 
                 hover_data=['sex', 'smoker', 'day', 'time', 'size'])

# Show the plot
fig.show()

"""


import plotly.express as px


fig = px.scatter(tips, x='total_bill', y='tip', title='Total Bill vs Tip')
fig.show()