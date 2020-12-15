import itertools
import numpy as np

file=open("input")
data=[int(i) for i in file.read().strip().split("\n")]

target=104054607

window=[0,1]
window_sum=0

while True:
	window_sum = np.sum(data[window[0]:window[1]])
	if window_sum==target:
		print(np.min(data[window[0]:window[1]]) + np.max(data[window[0]:window[1]]))
		exit()
	elif window_sum < target:
		window[1]+=1
	elif window_sum > target:
		window[0]+=1
