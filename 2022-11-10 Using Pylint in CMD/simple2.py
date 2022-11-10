'''
This is trying to fix simple1.py issues
'''
def myfunc():
    '''
    A Simple function
    '''
    first = 1
    second = 2
    print(first)
    print(second)


myfunc()

'''
Again; this was run in Pylint and I got:


(base) Desktop>python simple2.py
1
2

(base) Desktop>pylint simple2.py
************* Module simple2
simple2.py:5:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
simple2.py:8:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
simple2.py:9:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
simple2.py:10:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)
simple2.py:11:0: W0311: Bad indentation. Found 1 spaces, expected 4 (bad-indentation)

-----------------------------------
Your code has been rated at 1.67/10
___________________________________
After Changes I got
___________________________________


(base) Desktop>pylint simple2.py
************* Module simple2
simple2.py:35:0: C0304: Final newline missing (missing-final-newline)
simple2.py:16:0: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 7.14/10 (previous run: 1.67/10, +5.48)


'''