a = 1
b = 2
print(a)
print(b)


'''
I run this in CMD in two ways;
original and -r y (report, yes) which reports lots of extra info as following

(base) >pylint newpylint1.py
************* Module newpylint1
newpylint1.py:4:0: C0304: Final newline missing (missing-final-newline)
newpylint1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
newpylint1.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
newpylint1.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)

-----------------------------------
Your code has been rated at 0.00/10


(base) >pylint newpylint1.py -r y
************* Module newpylint1
newpylint1.py:4:0: C0304: Final newline missing (missing-final-newline)
newpylint1.py:1:0: C0114: Missing module docstring (missing-module-docstring)
newpylint1.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
newpylint1.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)


Report
======
4 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |5      |83.33 |NC       |NC         |
+----------+-------+------+---------+-----------+
|docstring |0      |0.00  |NC       |NC         |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |1      |16.67 |NC       |NC         |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |4      |4        |=          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |0      |0        |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-------------------------+------------+
|message id               |occurrences |
+=========================+============+
|invalid-name             |2           |
+-------------------------+------------+
|missing-module-docstring |1           |
+-------------------------+------------+
|missing-final-newline    |1           |
+-------------------------+------------+




------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)
'''