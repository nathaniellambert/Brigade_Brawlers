import sys
from cx_Freeze import setup, Executable

setup(
	name = "Brigade_Brawlers",
	version = "1.0",
	description = "A fun, single-player 8-bit fighter game!",
	executables = [Executable("interface.py",base = "Win32GUI")]
)
