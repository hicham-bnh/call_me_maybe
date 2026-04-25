import sys

if __name__ == "__main__":
	try:
		print(sys.argv[1])
	except Exception as e:
		print(e)