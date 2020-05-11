from matplotlib import pyplot as plt

''' this program teaches how to plot a very basic line chart using the matplotlib library by giving points as a list!!'''

# let us first plot a single line on the graph
# that means we need two points to the matplotlib; we can give those points either directly or in the form of lists as shown below

'''
# list of x-coordinates
x = [2,5]
# list of y-coordinates
y = [2,5]
plt.plot(x,y)
'''

# the very basic way to plot to lists using the plot function in pyplot
# plt.plot([1,5,2,3,4],[8,9,7,15,20])

# we can make two separate lists as well to store our data and then pass that to plot function to plot it; for example
l1 = [1,5,2,3,4]
l2 = [8,9,7,15,20]
#you will get the same output as the code written in the line 3
plt.plot(l1,l2) 
# show function is used to show the output on the screen
plt.show()