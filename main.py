import tkinter as tk


class MainWindow:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title('SPLDV')
        self.__root.geometry('250x140')

        # Frame Persamaan 1
        self.__frame = tk.Frame(self.__root)
        self.__frame.pack()

        # X Variable
        self.__x_value = tk.StringVar(self.__frame)
        self.__x_entry = tk.Entry(self.__frame, width=5)
        self.__x_entry.grid(row=0, column=0)
        self.__x_label = tk.Label(self.__frame, text="x")
        self.__x_label.grid(row=0, column=1)

        # Math Operation
        self.__math_op_options = ['+', '-']
        self.__math_op_value = tk.StringVar(self.__frame)
        self.__math_op = tk.OptionMenu(self.__frame, self.__math_op_value, *self.__math_op_options)
        self.__math_op.grid(row=0, column=2, padx=15)

        # Y Variable
        self.__y_value = tk.StringVar(self.__frame)
        self.__y_entry = tk.Entry(self.__frame, width=5)
        self.__y_entry.grid(row=0, column=3)
        self.__y_label = tk.Label(self.__frame, text="y")
        self.__y_label.grid(row=0, column=4)

        # Equal
        self.__y_label = tk.Label(self.__frame, text="=").grid(row=0, column=5)

        # Value Entry
        self.__value_inp = tk.StringVar(self.__frame)
        self.__value = tk.Entry(self.__frame, textvariable=self.__value_inp, width=5)
        self.__value.grid(row=0, column=6)

        # ===================================================================================================== #
        # ===================================================================================================== #
        # ===================================================================================================== #
        # ===================================================================================================== #
        # ===================================================================================================== #

        # Frame Persamaan 2
        self.__frame2 = tk.Frame(self.__root)
        self.__frame2.pack()

        # X Variable
        self.__x_value2 = tk.StringVar(self.__frame2)
        self.__x_entry2 = tk.Entry(self.__frame2, width=5)
        self.__x_entry2.grid(row=0, column=0)
        self.__x_label2 = tk.Label(self.__frame2, text="x")
        self.__x_label2.grid(row=0, column=1)

        # Math Operation
        self.__math_op_options2 = ['+', '-']
        self.__math_op_value2 = tk.StringVar(self.__frame2)
        self.__math_op2 = tk.OptionMenu(self.__frame2, self.__math_op_value2, *self.__math_op_options2)
        self.__math_op2.grid(row=0, column=2, padx=15)

        # Y Variable
        self.__y_value2 = tk.StringVar(self.__frame2)
        self.__y_entry2 = tk.Entry(self.__frame2, width=5)
        self.__y_entry2.grid(row=0, column=3)
        self.__y_label2 = tk.Label(self.__frame2, text="y")
        self.__y_label2.grid(row=0, column=4)

        # Equal
        self.__y_label2 = tk.Label(self.__frame2, text="=").grid(row=0, column=5)

        # Entry Value
        self.__value_inp2 = tk.StringVar(self.__frame2)
        self.__value2 = tk.Entry(self.__frame2, textvariable=self.__value_inp2, width=5)
        self.__value2.grid(row=0, column=6)

        # ===================================================================================================== #
        # ===================================================================================================== #
        # ===================================================================================================== #
        # ===================================================================================================== #
        # ===================================================================================================== #

        # Cal
        self.__cal = tk.Button(self.__frame2, text="Done!", command=self.jumlah, width=10)
        self.__cal.grid(row=1, columnspan=5, pady=10)

        # X Value
        self.__y_label = tk.Label(self.__frame2, text="X = null")
        self.__y_label.grid(row=2, column=0, columnspan=2)

        # Y Value
        self.__y_label = tk.Label(self.__frame2, text="Y = null")
        self.__y_label.grid(row=2, column=3, columnspan=2)

        self.__root.mainloop()

    def jumlah(self):
        x1 = self.__x_value.get()
        y1 = self.__y_value.get()
        r1 = self.__value_inp.get()

        x2 = self.__x_value2.get()
        y2 = self.__y_label2.get()
        r2 = self.__value_inp2.get()

        ypr1 = y1 * x2
        rpr1 = r1 * x2

        ypr2 = y2 * x1
        rpr2 = r2 * x1

        y = ypr1 - ypr2
        r = rpr1 - rpr2

        y_value = r / y
        x_value = int



hai = MainWindow()
