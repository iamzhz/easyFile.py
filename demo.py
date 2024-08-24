from easyFile import *
file = easyFile("example.txt")
file.set_mode(ReadAs.WORD)
file.apply_func(print)