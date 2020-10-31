from tkinter import *

calc = Tk()
calc.title('Calculator')
calc.iconbitmap('calculator.ico')
calc.resizable(False,False)
calc.configure(bg='#42444b', padx=5, pady=5)

# Entry field with set initial value to 0
entry_field = Entry(calc, bd=5, width=25, font=28, bg='#c6c6c8', justify='right')
entry_field.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10, columnspan=4)
entry_field.insert(0, 0)

# Defining the functions
class Calc():
  def __init__(self):
    self.total = 0
    self.current = ''
    self.op = ''
    self.input_value = True
    self.check_sum = False
    self.result = False

  def number_entry(self, num):
    self.result = False
    num1 = entry_field.get()
    num2 = str(num)
    if self.input_value: 
      self.current = num2
      self.input_value = False
    else:
      if num2 == '.':
        if num2 in num1:
          return
      self.current = num1 + num2
    self.display(self.current)
  
  def total_value(self):
    self.result = True
    self.current = float(self.current)
    if self.check_sum == True:
      self.valid_func()
    else:
      self.total = float(entry_field.get())


  def display(self, value):
    '''Checks if the value passed can be represented as an interger
      Deletes previous value and substitutes with the one passed'''
    entry_field.delete(0, END)
    entry_field.insert(0, value)

  def valid_func(self):
    '''Makes the operations and return a value formated in interg or float'''
    if self.op == 'add':
      self.total += self.current
    elif self.op == 'sub': 
      self.total -= self.current
    elif self.op == 'mult':
      self.total *= self.current
    elif self.op == 'div':
      self.total /= self.current
    elif self.op == 'power':
      self.total = (self.total ** self.current)
    
    self.input_value  = True
    self.check_sum = False

    if isinstance(self.total, int):
      self.total = (int(self.total))
    elif self.total.is_integer():
      self.total = (int(self.total))
    else:
      self.total = (float(self.total))
    self.display(self.total)

  def operation(self, op):
    self.current = float(self.current)
    if self.check_sum:
      self.valid_func()
    elif not self.result:
      self.total = self.current
      self.input_value = True
    self.check_sum = True
    self.op = op
    self.result = False

  def clear_entry(self):
    '''Clears the entry number but keeps the total'''
    self.result = False
    self.current = '0'
    self.display(0)
    self.input_value = True

  def clear(self):
    '''Clears the entry number and set the previous total to 0 clearing all values'''
    self.clear_entry()
    self.total = 0
    self.display(0)
    self.input_value = True

  def bkspace(self):
    '''Get the current number as a list and copy it without the last number'''
    if isinstance(self.current, float) or isinstance(self.current, int):
      self.clear_entry()
      self.display(0)
    elif self.current == '':
      self.display(0)
    else:
      self.current = self.current[:-1]
      self.display(self.current)

added_value = Calc() 

# Deffine number buttons and create a grid from row 2 ~ 5 columns 0 ~ 3 such as in a calculator
number_buttons = "789456123"
btn = []
i = 0
for r in range(2,5):
  for c in range(3):
    btn.append(Button(calc, width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b', text = number_buttons[i]))
    btn[i].grid(row=r, column=c, padx=1, pady=1)
    btn[i] ["command"] = lambda num = number_buttons[i]: added_value.number_entry(num)
    i += 1

# Defining other keys that use lambda
keys_dictWith = {'power': 'x'+chr(178), 'div': chr(247), 'mult': chr(215), 'add': '+', 'sub': '-'}
btn_lambda = []
j = 0
for k in keys_dictWith:
  btn_lambda.append(Button(calc, text=keys_dictWith[k], width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b'))
  btn_lambda[j]["command"] = lambda x = k: added_value.operation(x)
  j += 1

# Defining other keys that don't use lambda

btn_clear = Button(calc, command=added_value.clear, text='C', width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b')
btn_clearEntry = Button(calc, command=added_value.clear_entry, text='CE', width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b')
btn_bkspace = Button(calc, command=added_value.bkspace, text='<', width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b')

btn_0 = Button(calc, command=lambda: added_value.number_entry(0), text='0', width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b')
btn_dot = Button(calc, command=lambda: added_value.number_entry('.'), text='.', width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b')
btn_equal = Button(calc, command=added_value.total_value, text='=', width=6, height=1, font=12, bd=2, fg='mediumpurple', bg='#42444b')

# Buttons placement

btn_clear.grid(row=1, column=0, pady=1)
btn_clearEntry.grid(row=1, column=1, pady=1)
# sqrt
btn_lambda[0].grid(row=1, column=2, pady=1)
btn_bkspace.grid(row=1, column=3, pady=1)

# add
btn_lambda[3].grid(row=2, column=3, pady=1)

# mult
btn_lambda[2].grid(row=3, column=3, pady=1)

# sub
btn_lambda[4].grid(row=4, column=3, pady=1)

# div
btn_lambda[1].grid(row=5, column=2, pady=1)

btn_dot.grid(row=5, column=0, pady=1)
btn_0.grid(row=5, column=1, pady=1)
btn_equal.grid(row=5, column=3, pady=1)

calc.mainloop()

