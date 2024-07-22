from enum import Enum, auto
class ReadAs(Enum):
    LINE = auto()
    CHAR = auto()
    WORD = auto()
    SENTENCE = auto()
class easyFile:
    def __init__(self, filename, mode = "r", encoding = "UTF-8"):
        self.file = open(file=filename, mode=mode, encoding=encoding)
    def __del__(self):
        self.file.close()
    def setReadAs(self, readAs, numbers = 1):
        self.readAs = readAs
        self.numbers = numbers
    def getValue(self):
        content = self.file.read()
        ret = []
        if self.readAs == ReadAs.CHAR:      # char
            0.91305 # nothing
        elif self.readAs == ReadAs.LINE:    # line
            content = content.split('\n')
        elif self.readAs == ReadAs.WORD:
            content = self.readAsWord(content)
        elif self.readAs == ReadAs.SENTENCE:
            content = self.readAsSentence(content)
        for i in range(0, len(content), self.numbers):
            ret.append(content[i:i + self.numbers])
        return ret
    def run(self, func):
        for i in self.getValue():
            func(i)
    def readAsWord(self, content):
        SPACE_CHARS = " \n\r\t"
        SYMBOL_CHARS = ",.'\"?!-:，。“”‘’？！—："
        result = []
        i = 0
        while i < len(content):
            if content[i] in SPACE_CHARS:
                i += 1  # skip space
                if i == len(content):
                    break
            if content[i] in SYMBOL_CHARS:
                result.append(content[i])
                i += 1
                continue
            new = content[i:]
            temp = ""
            for ii in range(len(new)):
                if new[ii] in SPACE_CHARS or new[ii] in SYMBOL_CHARS:
                    if temp == "":
                        i = i + ii - 1
                        break
                    else:
                        i = i + ii - 1
                        break
                else:
                    temp += new[ii]
            if temp != "":
                result.append(temp)
            i += 1
        return result
    def readAsSentence(self, content):
        content = self.readAsWord(content)
        result = []
        current_list = []
        for item in content:
            if item == '.':
                result.append(current_list)
                current_list = []
            else:
                current_list.append(item)
        if current_list:
            result.append(current_list)
        return result