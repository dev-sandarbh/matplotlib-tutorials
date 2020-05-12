from matplotlib import pyplot as plt
''' in this tutorial we will learn about the bar-charts and histograms. 
A Bar Graph (also called Bar Chart) is a graphical display of data using bars of different heights.'''
# let us consider an example of students and their hobbies
# in format an id for a hobby => no of students
# for example, playing cricket has an id of 1 and it is hobby of 59 students; so we will have data as "1->59"

hobby_id = [1,2,3,4,5,6,7,8,9,10]
no = [59,22,15,50,36,74,45,68,5,40]

plt.bar(hobby_id,no,label='No of students having hobby id')
plt.xlabel("Hobby ID")
plt.ylabel("No. of students")
plt.title("Graph no of students vs. their hobbies represented as id no")
plt.legend()
plt.show()
# now we can also use bar-graphs to compare two data simultaneously!! Such as comparing marks of a student in Test 1 and in another Test 2. We will compare marks of a student in 5 subjects yearly.
marks_2018 = [58,99,67,84,78]
marks_2019 = [75,89,72,34,75]
sub_id1 = [1,3,5,7,9]
sub_id2 = [2,4,6,8,10]

# for marks 2018 we will use red color and for 2019 marks we will use green color
plt.bar(sub_id1,marks_2018,label='Marks Scored in Year 2018', color='red')
plt.bar(sub_id2,marks_2019,label='Marks Scored in Year 2019', color='green')
plt.title("Comparison of a student's marks scored in two consecutive years")
plt.legend()
plt.show()          #this gave us an overlapping chart because of same subject-id. So lets change that! Again run the program! 

''' we can give colours in matplotlib in various formats such as hex-code or predefined color names either in single letter or full-name. for example in place of red value we can also put 'r' or '#ff0000'. Similarly for green also! '''