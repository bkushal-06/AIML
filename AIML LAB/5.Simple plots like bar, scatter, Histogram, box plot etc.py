# 1. Bar Plot

import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 10]

# Create bar plot
plt.bar(categories, values, color='skyblue')
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()







## 2. Scatter Plot
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 5, 6]

# Create scatter plot
plt.scatter(x, y, color='red')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()





##3. Histogram
import matplotlib.pyplot as plt

# Data
data = [22, 55, 62, 45, 21, 22, 34, 42, 48, 55, 62, 68, 55, 48, 44, 45]

# Create histogram
plt.hist(data, bins=5, color='green', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.show()
 






## 4. Box Plot
import matplotlib.pyplot as plt

# Data
data = [22, 55, 62, 45, 21, 22, 34, 42, 48, 55, 62, 68, 55, 48, 44, 45]

# Create box plot
plt.boxplot(data)
plt.title('Box Plot Example')
plt.ylabel('Values')
plt.show()


