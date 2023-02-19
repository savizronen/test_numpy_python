import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(suppress=True) # to print results in non-scientific notation

# Q1
driver_fault = np.genfromtxt("../test_numpy_python/driverfault.csv", delimiter=",", skip_header=1)
print(driver_fault)

# Q2
rows = driver_fault.shape[0]
print(f"There are {rows} rows")

# Q3
sum_all = driver_fault[:, 1:].sum(axis=1)
sum_all = sum_all.reshape(rows, 1)
driver_fault = np.hstack([driver_fault, sum_all])
print(driver_fault)

# Q4
print(f"The max is {driver_fault[:, 8].max()}")

# Q5
regions = {1: 'south', 2: 'east', 3: 'north', 4: 'west', 5: 'center'}
reglist_names = list(regions.values())

speedlist = []
for k in regions:
    current_region_arr = driver_fault[driver_fault[:, 0] == k, 1]
    if len(current_region_arr) > 0:
        current_region_mean = np.mean(current_region_arr)
    else:
        current_region_mean = np.nan
    speedlist.append(current_region_mean)

print(reglist_names)
print(speedlist)


# Q6
plt.bar(reglist_names, speedlist)
plt.show()

# Bonus
mean_accident = driver_fault[:, 8].mean()
norths = driver_fault[(driver_fault[:, 0] == 3) & (driver_fault[:, 8] > mean_accident)]
print(norths)
