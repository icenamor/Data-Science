# Import matplotlib
import matplotlib.pyplot as plt

# Create scatter plot
plt.scatter(unemployment_rate, low_wage_jobs)

# Label x axis
plt.xlabel('Unemployment rate')

# Label y axis
plt.ylabel('Low pay jobs')

# Display the graph 
plt.show()

# Plot the red and triangle shaped scatter plot  
plt.scatter(dept_stats.unemployment_rate, dept_stats.low_wage_jobs, color="r", marker="^")

# Display the visualization
plt.show()

me lo apunto# Import matplotlib and pandas
import matplotlib.pyplot as plt
import pandas as pd

# Create scatter plot
dept_stats.plot(kind='scatter', x='unemployment_rate', y='low_wage_jobs')
plt.show()

# Import matplotlib and pandas
import matplotlib.pyplot as plt
import pandas as pd

# Create histogram
recent_grads.sharewomen.plot(kind='hist')
plt.show()

# DataFrame of non-college job sums
df = recent_grads.groupby(['major_category']).non_college_jobs.sum()

# Plot bar chart
df.plot(kind="bar")

# Show graph
plt.show()

# DataFrame of college and non-college job sums
df1 = recent_grads.groupby(['major_category'])['college_jobs','non_college_jobs'].sum()

# Plot bar chart
df1.plot(kind="bar")

# Show graph
plt.show()