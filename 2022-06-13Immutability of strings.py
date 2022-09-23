{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e87d1827",
   "metadata": {},
   "outputs": [],
   "source": [
    "name = \"Sam\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e4804512",
   "metadata": {},
   "outputs": [],
   "source": [
    "# name[0] = 'P' will get you an error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "37e64875",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'am'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "name[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a4e4924f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# we will slice it and assign"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "539cbf0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "last_letters = name[1:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1dccb2b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'am'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "last_letters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a0f82f8d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Pam'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'P' + last_letters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "dbf28cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# this is string concatenation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7e371c7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 'Hello World'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "5a36b734",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World it is beautiful outside!'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x + \" it is beautiful outside!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "885138d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "13a6dabf",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = x + \" it is beautiful outside!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0fe74d81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World it is beautiful outside!'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8d1d2672",
   "metadata": {},
   "outputs": [],
   "source": [
    "letter = 'z'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "05fbe208",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'zzzzzzzzzz'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "letter*10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "de70ee19",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2 + 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9e818171",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'23'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'2' + '3'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cd3c16da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# first will get you adding, the second is concatenation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "7ea84eec",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = \"Hello World\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "508bd510",
   "metadata": {},
   "outputs": [],
   "source": [
    "#x. + tab will get you a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f9e12f6e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HELLO WORLD'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "473a40c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "359af4ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "# x.upper it wont change the string by itself"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6fac8e0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#when you call it as x.upper with no (), python understands as a \"help\" and explains it to you"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "be415f84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function str.upper()>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.upper"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "81cd6a64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Hello', 'World']"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2fd3794e",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 'Hi this is a string'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "862941de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Hi', 'this', 'is', 'a', 'string']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "80af41b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['H', ' th', 's ', 's a str', 'ng']"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.split('i')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "22e8c992",
   "metadata": {},
   "outputs": [],
   "source": [
    "#now formatting for printing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0b11138d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print('Hello')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da335a20",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
