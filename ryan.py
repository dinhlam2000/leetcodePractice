import random
import numpy as py
from matplotlib import pyplot as plt

# 1. Create a list of 100,000 integers with values between 1 and 1000
original_list = list()
for element in range(100000):
    original_list.append(random.randint(1,1000))

# 2. Create a set from the list to remove any duplicates
my_set = set(original_list)

# 3. Create a dictionary from the set using the unique values as keys
count_dict = dict.fromkeys(my_set,0)

# 4. Use the original list and the dictionary to create a count of how many times each value appeared in the original
# list.

for item in original_list:
    # get the count
    newWeight = count_dict[item]
    # increment the count
    newWeight = newWeight + 1
    # update the count
    count_dict[item] = newWeight

print(count_dict)

# 5. Create lists from the keys and values and use these to create a scatter plot using matplotlib

lists = sorted(count_dict.items())
x,y = zip(*lists)
plt.plot(x,y)
plt.show()
