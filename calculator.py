{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d4d437a5-ff85-433e-8b17-4d35a57b26f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# calculator.py\n",
    "\n",
    "def add(x, y):\n",
    "\n",
    "    return x + y\n",
    "\n",
    "def subtract(x, y):\n",
    "\n",
    "    return x - y\n",
    "\n",
    "def multiply(x, y):\n",
    "\n",
    "    return x * y\n",
    "\n",
    "def divide(x, y):\n",
    "    if y == 0:\n",
    "        raise ValueError(\"Cannot divide by zero.\")\n",
    "    return x / y\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31f50d64-9aff-4c63-8286-d562fe0a7100",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
