a = 1
b = 2
print(a)
print(B) # mistake on purpose

# I ran pylint in CMD and got:
#/pylint simple1.py


# simple1.py:4:0: C0304: Final newline missing (missing-final-newline)
# simple1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# simple1.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# simple1.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# simple1.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

#-------------------------------------
#Your code has been rated at -12.50/10


# Pylint is accusing lots of style issues and found the error in the program.