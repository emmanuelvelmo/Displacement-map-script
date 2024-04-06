from cx_Freeze import setup, Executable

setup(
    name="Displacement map",
    version="1.0",
    description="Displacement map script",
    executables=[Executable("Displacement map.py")]
)