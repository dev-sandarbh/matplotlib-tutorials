from matplotlib import pyplot as plt
import random
''' in this tutorial we will learn how to plot a histogram using matplotlib.pyplot'''
''' so to understand the histogram we will take up  an example of height of trees in amazon forest!. Basically we are doing so because histograms are generally used to represent a continous distribution of data. So We will consider height of 100 trees represented in meters. To get some random height values we will use the random module. '''


# this list comprehension will generate a list of height of 100 trees 
t_height = [random.randint(25,150) for h in range(100)]
# print(t_height)
# print(len(t_height))

# let us give some frequency distribution over a gap of 10meters continously. To do so we will use "bins" arg. Bin means the distribution containing box or the continous gap which we see in a frequency distribution!
# this list comprehension will give us a continous frequency distribution of a gap of 10.
bins = [i for i in range(0,160,10)]
# print(bins)

# let's plot the continous histogram for our tree height data
plt.hist(t_height,bins,label='Continous Distribution of Tree Height Of Amazon Forest',color='#00cc66',histtype='step',orientation='horizontal')
plt.xlabel('Range Distributed by 10meters')
plt.ylabel('No of Trees')
plt.legend()
plt.show()


''' 
rwidth -- attribute which signifies the width of the bar to be displayed; if set to 1 there will be overlapping and no clear boundary will be visible!

histtype -- attribute give us different types of histograms to be drawn. Standard Values can be {'bar', 'barstacked', 'step', 'stepfilled'}.

orientation -- attribute tells us wether to align our histogram as horizontal or vertical!

SO we can different combinations of histtype and orientations!

Remember that rwidth is ignored with step and stepfilled histtype-values!!
'''