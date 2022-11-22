import tkinter as tk
from tkinter import END
from tkinter.scrolledtext import ScrolledText


class MainWindow:
    def __init__(self, run=True, run_program=lambda: None):
        self.window = window = tk.Tk()
        window.title("ELang IDLE")
        window.geometry("720x580")

        self.code_text = ScrolledText(window)
        self.code_text.pack(fill="x")
        input_frame = tk.LabelFrame(window, text="IN")
        tk.Button(input_frame, text="Run code", command=run_program).pack(side=tk.LEFT)
        tk.Label(input_frame, text="Input:").pack(side=tk.LEFT)
        self.input_text = tk.Text(input_frame, height=1)
        self.input_text.pack(fill="x", side=tk.LEFT)
        input_frame.pack(fill="x")
        output_frame = tk.LabelFrame(window, text="OUT")
        self.output_text = ScrolledText(output_frame, state=tk.DISABLED)
        self.output_text.pack(fill="x", side=tk.TOP)
        output_frame.pack(fill="x")
        self.write_output("Programming language IDLE v0.1")

        if run:
            self.mainloop()

    def mainloop(self):
        self.window.mainloop()

    def write_output(self, text, end="\n"):
        self.output_text.configure(state='normal')
        self.output_text.insert(tk.INSERT, str(text)+end)
        self.output_text.configure(state='disable')
        self.output_text.yview(END)

    def get_text_code(self):
        return self.code_text.get(1.0, tk.END)

    def write_code(self, text):
        self.code_text.insert(tk.INSERT, text)

    def get_text_output(self):
        return self.output_text.get(1.0, tk.END)

    def get_input_text(self):
        return self.input_text.get(1.0, tk.END)

    def set_input_text(self, text):
        self.input_text.delete(1.0, tk.END)
        self.input_text.insert(tk.INSERT, text)


if __name__ == '__main__':
    MainWindow(run=True)
