from matplotlib import pyplot as plt

''' this program teches us to plot a line graph with legends and title on the output screen'''
x1 = [2,5,8]
y1 = [2,5,8]

x2 = [5,10,15]
y2 = [7,13,18]

plt.xlabel('X-COORDINATES')
plt.ylabel('Y-COORDINATES')

plt.title('First Line Graph\nSecond Line Also Included')

# this label keyword argument is issed to get the legend in a graph
plt.plot(x1,y1,label='First Line')
plt.plot(x2,y2,label='Second Line')

# gives the legends/refernces to the different lines/plots on the same output screen 
plt.legend()
plt.show()