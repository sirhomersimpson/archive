#!/usr/bin/env python
import argparse

"""
https://realpython.com/command-line-interfaces-python-argparse/
"""

def main():
	parser = argparse.ArgumentParser(description='Test123')
	parser.add_argument('--input', '-i', action='store', type=int, help='a number')
	parser.add_argument('--output', '-o', action='store', type=str, help='a number')
	
	args = parser.parse_args()
	print(args.input)
	print(args.output)
	print(vars(args))


if __name__ == '__main__':
	main()