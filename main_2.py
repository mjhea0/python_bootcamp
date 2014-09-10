import main_1

print ("top-level in main_2.py")
main_2.func()

if__name__ == "__main__":
	print("main_2.py is being run directly")
else:
	print("main_2.py is being imported into another module")
