class TextStat:
    def __init__(self, c, l, w, s, wh):
        self.chars = c
        self.letters = l
        self.words = w
        self.sentences = s
        self.whitespaces = wh
    def __str__(self):
        return str(self.__dict__)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

def text_statistics(s):
    stats = TextStat(len(s), 0, 0, 0, 0)
    for i in range(0, len(s)):
        if s[i].isalpha():
            stats.letters += 1
        if s[i].isalpha() and not s[i+1].isalpha():
            stats.words += 1
        if s[i] == '.' or s[i] == '!' or s[i] == '?':
            stats.sentences += 1
        if s[i].isspace():
            stats.whitespaces += 1
    return stats


CheckResult.check(text_statistics('Just a short String.'), TextStat(20, 16, 4, 1, 3))
CheckResult.check(text_statistics("Very! Short. One?"), TextStat(17, 12, 3, 3, 2))
CheckResult.check(text_statistics("To\tcheck\rWhitespace."), TextStat(20, 17, 3, 1, 2))
CheckResult.check(text_statistics("What shall\nwe test?"), TextStat(19, 15, 4, 1, 3))
CheckResult.check(text_statistics("Last! one!"), TextStat(10, 7, 2, 2, 1))
