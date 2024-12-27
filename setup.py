from cx_Freeze import setup, Executable

setup(name="Displacement map", executables=[Executable("Displacement map.py")], options={"build_exe": {"excludes": ["tkinter"]}})
