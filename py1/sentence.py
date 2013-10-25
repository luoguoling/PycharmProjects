__author__ = 'luoguoling'
class ParserError(Exception):
    pass
class Sentence(object):
    def __init__(self,subject,verb,object):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None
    def match(word_list,expecting):
        if word_list:
            word = word_list.pop(0)
            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(word_list,word_type):
        while word_list.peek(word_list) == word_type:
            word_list.match(word_list,word_type)

    peek()
    match()
    skip()
s = Sentence('aaa','is','bbb')
print s.object,s.verb,s.subject
print s.peek('aa')





