'''this is worked example from stackoverflow to 
undersatnd why we use the main routine'''

def func():
	print ("func() in main_1.py")

print("top-level in main_1.py")

if __name__=="__main__":
    print("main_1.py is being run directly")

else:
    print("main_1.py is being imported into another module")
        	
