{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c874bf0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is a string INSERTED\n"
     ]
    }
   ],
   "source": [
    "print('This is a string {}'.format('INSERTED'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6a8f09b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# .format will insert between{}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e93483ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The fox brown quick\n"
     ]
    }
   ],
   "source": [
    "print('The {} {} {}' .format('fox', 'brown', 'quick'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cb8f67a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The quick brown fox\n"
     ]
    }
   ],
   "source": [
    "print('The {2} {1} {0}' .format('fox', 'brown', 'quick'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "13f8e57f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The fox fox fox\n"
     ]
    }
   ],
   "source": [
    "print('The {0} {0} {0}' .format('fox', 'brown', 'quick'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d2ca7dd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The quick brown fox\n"
     ]
    }
   ],
   "source": [
    "print('The {q} {b} {f}' .format(f='fox', b='brown', q='quick'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9302e9e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#note that if the braces{} have nothing in it, you will get an error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4965c45c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The fox fox fox\n"
     ]
    }
   ],
   "source": [
    "print('The {f} {f} {f}' .format(f='fox', b='brown', q='quick'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b37c0e8",
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
