import word
import random

class Sentence():
    def __init__(self):
        print('Sentence created')

    def fromFormatToString(self, li):
        s = ""
        for i in li:
            try:
                hh = i[0].get("label", "")
                s += f'{hh} '
            except BaseException:
                pass
        strlen = s.__len__() - 1
        s = s[0:strlen]
        return s.capitalize()

    def createQuestionSentence(self):
        print("lol")

    def createNormalSentence(self):
        a = random.randint(0, 2)
        if (a == 0): # просто подлежащие и сказуемое
            listWords = []
            generator = word.Word()
            w = generator.createPronoun(0, listWords)
            listWords.append(w)
            w = generator.createVerb(listWords)
            listWords.append(w)
            del generator
            return self.fromFormatToString(listWords)
        elif (a == 1):
            listWords = []
            generator = word.Word()
            w = generator.createPronoun(0, listWords)
            listWords.append(w)
            w = generator.createVerb(listWords)
            listWords.append(w)
            w = generator.createAddiction(listWords)
            listWords.extend(w)
            del generator
            return self.fromFormatToString(listWords)
        elif (a == 2):
            listWords = []
            generator = word.Word()
            w = generator.createPronoun(0, listWords)
            listWords.append(w)
            w = generator.createVerb(listWords)
            listWords.append(w)
            w = generator.createAddiction(listWords)
            listWords.extend(w)

            w = generator.createAdverb()
            listWords.append(w)
            generator = word.Word()
            w = generator.createPronoun(0, listWords)
            listWords.append(w)
            w = generator.createVerb(listWords)
            listWords.append(w)
            w = generator.createAddiction(listWords)
            listWords.extend(w)
            del generator
            return self.fromFormatToString(listWords)
        elif (a == 3):
            print("lol")
        elif (a == 4):
            print("lol")
        elif (a == 5):
            print("lol")