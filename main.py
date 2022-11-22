from WindowIDLE import MainWindow
from AlgoCompilerOf12 import AlgoCompiler, code


def _print(*args, end="\n", sep=" "):
    global window
    if args:
        window.write_output(sep.join(map(str, args)), end=end)


def compile_code():
    global window
    _print("="*15, "RUN CODE", "="*15)
    result = AlgoCompiler(window.get_text_code(), window.get_input_text(), _debug_print=_print).compile()
    _print("RESULT:", result)


if __name__ == '__main__':
    window = MainWindow(run_program=compile_code, run=False)
    window.write_code(code)
    window.set_input_text("1"*66)
    window.mainloop()
