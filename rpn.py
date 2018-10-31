#!/usr/bin/env python3
import operator

op = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
}
def calculate(arg):
	#stack
	stack = []
	#tokenize
	tokens = arg.split()
	# process tokens
	for token in tokens:
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			val1 = stack.pop()
			val2 = stack.pop()
			func = op[token]
			result = func(val2, val1)

			stack.append(result)
			return stack[0]

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print(result)

if __name__ == '__main__':
	main()
