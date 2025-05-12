import tkinter as tk
from tkinter import ttk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        # Переменные для хранения данных
        self.current_input = tk.StringVar()
        self.result_var = tk.StringVar()
        self.operation = None
        self.first_number = 0

        # Создание интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Поле ввода
        entry_frame = ttk.Frame(self.root)
        entry_frame.pack(pady=10)

        self.entry = ttk.Entry(
            entry_frame,
            textvariable=self.current_input,
            font=("Arial", 14),
            justify="right",
        )
        self.entry.pack()

        # Поле вывода результата (неактивное)
        result_frame = ttk.Frame(self.root)
        result_frame.pack(pady=5)

        ttk.Label(result_frame, text="Результат:").pack(side="left")
        self.result = ttk.Entry(
            result_frame,
            textvariable=self.result_var,
            font=("Arial", 14),
            justify="right",
            state="readonly",
        )
        self.result.pack()

        # Кнопки цифр и операций
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=15)

        # Расположение кнопок в сетке
        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("0", 3, 0),
            ("C", 3, 1),
            ("=", 3, 2),
            ("+", 3, 3),
        ]

        for text, row, col in buttons:
            # Общие параметры для всех кнопок
            btn_params = {
                "text": text,
                "font": ("Arial", 12, "bold"),
                "bg": "#2196F3",  # голубой фон
                "fg": "white",  # белый текст
                "activebackground": "#1976D2",  # темно-голубой при нажатии
                "relief": tk.RAISED,
                "borderwidth": 3,
                "command": lambda t=text: self.on_button_click(t),
            }

            # Особые параметры для кнопки "="
            if text == "=":
                btn_params.update(
                    {
                        "bg": "#4CAF50",  # зеленый фон
                        "activebackground": "#45a049",
                    }
                )

            btn = tk.Button(buttons_frame, **btn_params)
            btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

    def on_button_click(self, text):
        if text in "0123456789":
            current = self.current_input.get()
            self.current_input.set(current + text)
        elif text == "C":
            self.current_input.set("")
            self.result_var.set("")
            self.operation = None
        elif text in "+-*/":
            if self.current_input.get():
                self.first_number = float(self.current_input.get())
                self.operation = text
                self.current_input.set("")
        elif text == "=":
            if self.current_input.get() and self.operation:
                second_number = float(self.current_input.get())
                try:
                    if self.operation == "+":
                        res = self.first_number + second_number
                    elif self.operation == "-":
                        res = self.first_number - second_number
                    elif self.operation == "*":
                        res = self.first_number * second_number
                    elif self.operation == "/":
                        res = self.first_number / second_number

                    self.result_var.set(str(res))
                    self.current_input.set("")
                    self.operation = None
                except ZeroDivisionError:
                    self.result_var.set("Ошибка")
                    self.current_input.set("")
                    self.operation = None


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
