# easyFile

It's a project(just one file) to read a file easily. Even though it's not very useful.  
And it's just for fun.

## Usage

```python
from easyFile import *
# open a file
file = easyFile("path/to/file.txt")
# set read mode
file.set_mode(ReadAs.WORD)
# read the file word by word and print it as a list
file.apply_func(print)
```
The program will output something like:

```
['Hi']
['there']
['Glad']
['to']
['see']
['you']
```