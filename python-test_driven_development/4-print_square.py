#!/usr/bin/python3
"""Module for print_square function"""

def print_square(size):
	"""prints a square with the character #

	Args:
		size (int): size of square with equal sides
	"""
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	elif size < 0:
		raise TypeError("size must be >= 0")
	elif size == 0:
		print("")  # print newline for size=0
	else:
		for i in range(size):
			for i in range(size):
				print("#", end="")  # print "#"
			print("")  # print new line
