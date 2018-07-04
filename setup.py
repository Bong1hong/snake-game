import cx_Freeze
import os

os.environ["TCL_LIBRARY"] = "C:\\Python\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Python\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Snake Game",
    options={"build_exe": {"packages":["pygame"], "include_files":["game.py","gameobject.py","hitbox.py","render.py","apple.png", "bomb.png", "snake head.png"]}},
    description = "Snake Game",
    executables = executables,
    version="22.99"
    )
