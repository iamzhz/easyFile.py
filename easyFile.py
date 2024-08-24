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

    def set_mode(self, readAs, numbers = 1):
        self.readAs = readAs
        self.numbers = numbers

    def get_content(self):
        content = self.file.read()
        ret = []
        if self.readAs == ReadAs.CHAR:      # char
            # nothing
            pass
        elif self.readAs == ReadAs.LINE:    # line
            content = content.split('\n')
        elif self.readAs == ReadAs.WORD:
            content = self.to_words(content)
        elif self.readAs == ReadAs.SENTENCE:
            content = self.to_sentences(content)
        num_content = len(content)
        for i in range(0, min(num_content, len(content) // self.numbers * self.numbers), self.numbers):  
            ret.append(content[i:i + self.numbers])
        return ret

    def apply_func(self, func):
        for i in self.get_content():
            func(i)

    def to_words(self, content):
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
            start = i
            while i < len(content) and (content[i] not in SPACE_CHARS and content[i] not in SYMBOL_CHARS):  
                i += 1
            if start!= i:
                result.append(content[start:i])
            i += 1
        return result

    def to_sentences(self, content):
        content = self.to_words(content)
        result = []
        current_list = []
        end_sentence_chars = ['.', '!', '?']  
        for item in content:
            if item in end_sentence_chars:
                result.append(current_list)
                current_list = []
            else:
                current_list.append(item)
        if current_list:
            result.append(current_list)
        return result