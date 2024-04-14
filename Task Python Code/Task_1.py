from scipy.stats import bernoulli
import matplotlib.pyplot as plt

#Instance of Bernoulli distribution with parameter p=0.74
bd=bernoulli(0.74)

#for the visualization of thr bar plot of Bernoulli's distribution
plt.figure(figsize=(10,10))
plt.xlim(-2,2)
plt.bar(x,bd.pmf(x),color='blue')

#for labeling the Bar Plot
plt.title('Proportion of “for” and “against” using a bar graph)', fontsize='12')
plt.xlabel('Values of random variable x (0, 1)', fontsize='12')
plt.ylabel('Probability', fontsize='12')
plt.show()

#for labeling the pie chart
size=[0.74,1-0.74]
plt.figure(figsize=(10,10))
plt.title('Proportion of “for” and “against” using a percentage', fontsize='12')
Mlabels = 'Vote for', 'Vote Against'
mcolor='Green','Red'
plt.pie(size,colors=mcolor, labels = Mlabels,autopct='%1.1f%%',shadow=True, startangle=90)
plt.show()