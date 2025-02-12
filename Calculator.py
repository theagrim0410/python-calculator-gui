
from tkinter import *
import math


window = Tk()
window.title('Calculator')
window.configure(bg="#34495E") 
window.geometry("350x400")

# Title Label
Label(window, text='My Calculator', fg='white', bg="#34495E",
      font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

# Labels
Label(window, text='First Number:', fg="white", bg="#34495E", font=('Arial', 10)).grid(row=1, column=0, padx=10, pady=5, sticky=E)
Label(window, text='Second Number:', fg="white", bg="#34495E", font=('Arial', 10)).grid(row=2, column=0, padx=10, pady=5, sticky=E)
Label(window, text='Operator:', fg="white", bg="#34495E", font=('Arial', 10)).grid(row=3, column=0, padx=10, pady=5, sticky=E)
Label(window, text='Answer:', fg="white", bg="#34495E", font=('Arial', 10)).grid(row=4, column=0, padx=10, pady=5, sticky=E)

# Entry fields
E1 = Entry(window, bd=4, font=('Arial', 10))
E1.grid(row=1, column=1, padx=10, pady=5)
E2 = Entry(window, bd=4, font=('Arial', 10))
E2.grid(row=2, column=1, padx=10, pady=5)
E3 = Entry(window, bd=4, font=('Arial', 10))
E3.grid(row=3, column=1, padx=10, pady=5)
E4 = Entry(window, bd=4, font=('Arial', 10), state='readonly')
E4.grid(row=4, column=1, padx=10, pady=5)

# Function to perform calculations
def calculate():
    num1 = E1.get().strip()
    num2 = E2.get().strip()
    operator = E3.get().strip()

    if not num1 or not num2 or not operator: 
        answer = "Fields cannot be empty!"
    else:
        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                answer = num1 + num2
            elif operator == "-":
                answer = num1 - num2
            elif operator == "*":
                answer = num1 * num2
            elif operator == "/":
                answer = "Cannot divide by zero!" if num2 == 0 else num1 / num2
            elif operator == "**":
                answer = num1 ** num2
            elif operator == "%":
                answer = (num1 * num2) / 100
            elif operator.lower() == "log":
                answer = math.log(num1, num2)
            else:
                answer = "Invalid Operator!"
        except ValueError:
            answer = "Invalid input!"

    # Display result
    E4.config(state='normal')
    E4.delete(0, END)
    E4.insert(0, answer)
    E4.config(state='readonly')

# Buttons
Button(window, text="Calculate", command=calculate, bg='#27AE60', fg='white', font=('Arial', 12, 'bold'),
       bd=6, width=12).grid(row=5, column=0, columnspan=2, pady=15)

Button(window, text="Close", command=window.destroy, bg='#E74C3C', fg='white', font=('Arial', 12, 'bold'),
       bd=6, width=12).grid(row=6, column=0, columnspan=2, pady=5)

window.mainloop()
