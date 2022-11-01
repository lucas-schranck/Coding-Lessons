#one.py
#print('Hello')

#python won't run main on top of your script

#build-in variable called name assigns a string; if run in cmd, it'll assign __name__ = "__main__"
#therefore you can try checking if name and main are same (usually at the end of the script)
#if __name__ == "__main__":
#	myfunc()


def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

#now I can check if it's being called directly like this:
if __name__ == '__main__':
	print("ONE.PY is being run directly!")
else:
	print("ONE.PY has been imported")


#now in CMD
#I run: python one.py
#I get: TOP LEVEL IN ONE.PY
#I get: ONE.PY is being run directly!

#the true idea behind calling name=main is that we organize our code;
#you put lots of logic and func up in the code, and down below, you call them