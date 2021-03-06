import random
r = random.randint(1,100)
r = int(r)
count = 0
while True:
	count += 1
	num = input('please guess number')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		break
	elif num > r :
		print('答案比數字小')
	elif num < r:
		print('答案比數字大')

	print('this is your', count, 'times')