def square(number):
	"""Takes the number and multiplies it by itself to get the square"""
	sqr_num = number * number

	return sqr_num

def returndifference(num1, num2):
	"""Takes two numbers and returns the difference"""
	return num1 - num2

def cube(num3):
	"""Take a number and multiplies that number by itself twice"""

	cube_number= num3 * num3 * num3

	return cube_number

def multiply(num4, num5):
	"""Take two numbers and multiply them and return the result"""
	multinumber =  num4 * num5

	return multinumber







input_num = 5
output_num = square(input_num)

print output_num

output_num2 = returndifference(3, 5)

print output_num2

output_num3 = cube(5)

print output_num3

output_num4 = int(multiply(3, 3))

print output_num4