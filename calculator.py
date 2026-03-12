import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(self, width=312, height=272.5, bg="grey")
        buttons_frame.pack()

        # first row
        clear = tk.Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.clear())
        clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = tk.Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("/"))
        divide.grid(row=0, column=3, padx=1, pady=1)

        # second row
        seven = tk.Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("7"))
        seven.grid(row=1, column=0, padx=1, pady=1)
        eight = tk.Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("8"))
        eight.grid(row=1, column=1, padx=1, pady=1)
        nine = tk.Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("9"))
        nine.grid(row=1, column=2, padx=1, pady=1)
        multiply = tk.Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("*"))
        multiply.grid(row=1, column=3, padx=1, pady=1)

        # third row
        four = tk.Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("4"))
        four.grid(row=2, column=0, padx=1, pady=1)
        five = tk.Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("5"))
        five.grid(row=2, column=1, padx=1, pady=1)
        six = tk.Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("6"))
        six.grid(row=2, column=2, padx=1, pady=1)
        subtract = tk.Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("-"))
        subtract.grid(row=2, column=3, padx=1, pady=1)

        # fourth row
        one = tk.Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("1"))
        one.grid(row=3, column=0, padx=1, pady=1)
        two = tk.Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("2"))
        two.grid(row=3, column=1, padx=1, pady=1)
        three = tk.Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("3"))
        three.grid(row=3, column=2, padx=1, pady=1)
        add = tk.Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("+"))
        add.grid(row=3, column=3, padx=1, pady=1)

        # fifth row
        zero = tk.Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("0"))
        zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = tk.Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.press("."))
        point.grid(row=4, column=2, padx=1, pady=1)
        equals = tk.Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.equal())
        equals.grid(row=4, column=3, padx=1, pady=1)

    def press(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")


if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()
