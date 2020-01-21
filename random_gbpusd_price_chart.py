#random_gbp_price.py

import random
import matplotlib.pyplot as plt 
#open_price = random.randrange(1, 200, 3)
base_price = 16000
x_list = []
y_list = []

close_price = 0

for i in range(400):
	x = random.randrange(-60, 60, 3)
	close_price = close_price + x

	print(i, x, close_price)
	x_list.append(close_price)
	y_list.append(i)

# plotting the points  
plt.plot(y_list, x_list) 
  
# naming the x axis 
plt.ylabel('GBP/USD price') 
# naming the y axis 
plt.xlabel('nth day') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 	
