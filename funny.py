import random as r
import string
import os
import tkinter as tk

# create a window
window = tk.Tk()
window.title("Funny")
window.geometry("740x500")


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#print 
print('The funny generator 1.0')
length = int(input('How many characters do you want? '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special = string.punctuation

#combine the data
data = lower + upper + numbers + special

#use random
password = ''.join(r.choice(data) for x in range(length))

clearConsole()
print('Your password is: ' + password)