data = [(2,4), (4,6), (6,8), (8,4), (10,3), (12,6), (14,10)]

grid_height = 10
grid_length = 16

def should_render(i,j):
	selected_tuple = (-1,-1)
	for iterator in data:
		if(iterator[0] == j):
			selected_tuple = iterator

	if(selected_tuple[0] == -1):
		return False

	if(grid_height - selected_tuple[1] - 1 <= i):
		return True

	return False

for i in range(grid_height):
	for j in range(grid_length):
		if(i==grid_height-1 or j==0):
			print('*',end='')
		elif(should_render(i,j)):
			print('#',end='')
		else:
			print(' ',end='')
	print()

