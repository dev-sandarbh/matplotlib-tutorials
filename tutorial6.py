from matplotlib import pyplot as plt
import random
''' in this tutorial we will learn about some more attributes that we get to use when we plot graphs such as linewidth, linestyle, marker, markersize, markeredgecolor,etc.'''

marks_1 = [random.randint(15,100) for m in range(10)] 
marks_2 = [random.randint(15,100) for n in range(10)]
sub = [s for s in range(10)]

plt.xlabel("Subjects of students")
plt.ylabel("Marks of students")

plt.plot(sub,marks_1,color="red",linewidth=3,linestyle="dashed",marker='+',markeredgecolor='green',label="Marks of Student 1")
plt.plot(sub,marks_2,color="cyan",linewidth=3,linestyle="dashed",marker='*',markeredgecolor='orange',label="Marks of Student 2")
plt.title("Comparison of Marks of Two Students")
plt.legend(loc="upper right")
plt.show()

''' also we can save our figure by writing a single line of code as shown:
plt.savefig("C:\\your\\path\\your\\folder\\name_of_figure.png")
'''