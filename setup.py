from cx_Freeze import setup, Executable
base = None
executables = [Executable("index.py", base=base)]
packages = ["tkinter", "math", "time"]

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="morpion",
    options=options,
    version="1.0",
    description='Voici mon programme',
    executables=executables
)
