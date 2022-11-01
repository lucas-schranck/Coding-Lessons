#two.py

import one

print("TOP LEVEL IN TWO.PY")

one.func()

#again; we'll see if this is being run directly or being imported
if __name__ == '__main__':
	print("TWO.PY is being run directly")
else:
	print("TWO.PY has been imported")

#now in CMD

#I run: python two.py
#I get: TOP LEVEL IN ONE.PY
#I get: ONE.PY has been imported
#I get: TOP LEVEL IN TWO.PY
#I get: FUNC() IN ONE.PY
#I get: TWO.PY is being run directly
