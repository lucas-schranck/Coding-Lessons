import unittest
import cap

class TestCap(unittest.TestCase): # inheritance from unittest.testcase; create class

	def test_one_word(self): # now you have a function to be called (test_one)
		text = 'python' 
		result = cap.cap_text(text) # importing cap and importing cap_text function from cap.py // call whatever func from script
		self.assertEqual(result, 'Python') # this is what is expected

	def test_multiple_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
	unittest.main()



''' 
I run (def cap_text was using method .capitalize, not .title):

>python test_cap.py

	I got:

F.
======================================================================
FAIL: test_multiple_words (__main__.TestCap)
----------------------------------------------------------------------
Traceback (most recent call last):
  \test_cap.py", line 14, in test_multiple_words
    self.assertEqual(result, 'Monty Python')
AssertionError: 'Monty python' != 'Monty Python'
- Monty python
?       ^
+ Monty Python
?       ^


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
______________________________________________________________________
I run def cap_text using method .title now;

I got:

>python test_cap.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

'''