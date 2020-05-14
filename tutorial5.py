from matplotlib import pyplot as plt

''' in this tutorial we will learn how to plot a pie chart and what all attributes it comes with!'''

# basic information regarding pie charts
'''
Pie Chart: a special chart that uses "pie slices" to show relative sizes of data.
So to learn pie charts, we will take an example of total number of hours we devote to our different activities during a day! 
'''

# slices means fractions of total number of hours/fraction of activity you do
slices = [5,2,4,10,3]
# list of activites to be used as labels on the pie chart
act = ['sleeping','reading','playing','coding','miscellaneous']
# col is a list a colours that we are going to pass
col = ['#00ff80','#0066ff','#ff8000','#ff3385','#33cccc']

plt.pie(slices,labels=act,colors=col,startangle=0,shadow=True,explode=(0,0,0,0.1,0),autopct='%1.1f%%')

# plt.legend()
plt.title("Distribution of Time in Different Activites")
plt.show()

''' 
Other attributes added are:-
startangle-> denotes the starting angle position of the pie chart
shadow -> gives us a shadow at the bottom and around the chart
explode -> means cuts-out the selected portion to make it more attractive
autopct-> adds percentage to the different fractions specified! 
'''

