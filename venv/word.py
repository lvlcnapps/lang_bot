import random
import json

class Word():
    def __init__(self):
        fileOp = open("verbs.txt", 'r')
        self.verbsList = json.loads(fileOp.read())
        fileOp.close()
        #print('Word created')

    def __del__(self):
        pass

    # Местоимение
    def createPronoun(self, case, lastWords):
        if case == 0:

            t = random.randint(0, 1)

            l = [[{
                    "label": "я",
                    "type": 1,
                    "time": t,
                    "sex": 0,
                    "face": 0,
                    "multi": 0
                }],
                [{
                    "label": "ты",
                    "type": 1,
                    "time": t,
                    "sex": 0,
                    "face": 1,
                    "multi": 0
                }],
                [{
                    "label": "ты",
                    "type": 1,
                    "time": t,
                    "sex": 1,
                    "face": 1,
                    "multi": 0
                }],
                [{
                    "label": "он",
                    "type": 1,
                    "time": t,
                    "sex": 0,
                    "face": 2,
                    "multi": 0
                }],
                [{
                    "label": "она",
                    "type": 1,
                    "time": t,
                    "sex": 1,
                    "face": 2,
                    "multi": 0
                }],
                [{
                    "label": "мы",
                    "type": 1,
                    "time": t,
                    "sex": 0,
                    "face": 0,
                    "multi": 1
                }],
                [{
                    "label": "вы",
                    "type": 1,
                    "time": t,
                    "sex": 0,
                    "face": 1,
                    "multi": 1
                }],
                [{
                    "label": "вы",
                    "type": 1,
                    "time": t,
                    "sex": 1,
                    "face": 1,
                    "multi": 1
                }],
                [{
                    "label": "они",
                    "type": 1,
                    "time": t,
                    "sex": 0,
                    "face": 2,
                    "multi": 1
                }],
                [{
                    "label": "они",
                    "type": 1,
                    "time": t,
                    "sex": 1,
                    "face": 2,
                    "multi": 1
                }]
            ]
            a = random.randint(0, 9)
            try:
                if (lastWords[0][0].get("type", -1) == 1):
                    while (l[a][0].get("face") == lastWords[0][0].get("face")):
                        a = random.randint(0, 9)
            except BaseException:
                pass
            try:
                tt = lastWords[-1][0].get("time", -1)
                #print(tt)
                if (tt != -1):
                    l[a][0]["time"] = tt
            except BaseException:
                pass
            #print(l[a])
            return l[a]
        return []

    # Глагол
    def createVerb(self, lastWords):
        if lastWords.__len__() != 0:
            k = lastWords[lastWords.__len__() - 1][0]
            f = k.get("face", -1)
            if f != -1:
                a = random.randint(0, self.verbsList.__len__() - 1)
                id = self.verbsList[a].pop()
                # print(id)
                w = self.verbsList[a]
                w = w[k.get("multi", -1) + 1]
                #print(w)
                if not isinstance(w, str):
                    if w.__len__() != 1:
                        w = w[k.get("time")]
                        #print(w)
                        if not isinstance(w, str):
                            if w.__len__() != 1:
                                if k.get("time") == 0:
                                    w = w[k.get("face")]
                                    #print(w)
                                    if not isinstance(w, str):
                                        if w.__len__() != 1:
                                            w = w[k.get("sex")]
                                            #print(w)
                                        else:
                                            w = w[0]
                                else:
                                    w = w[k.get("sex")]
                                    #print(w)
                                    if not isinstance(w, str):
                                        if w.__len__() != 1:
                                            w = w[k.get("face")]
                                            #print(w)
                                        else:
                                            w = w[0]
                            else:
                                w = w[0]
                    else:
                        w = w[0]
                self.verbsList[a].append(id)
                #print(w)
                return [{
                    "label": w,
                    "type": 2,
                    "time": k.get("time", 0),
                    "sex": k.get("sex", 0),
                    "face": k.get("face", 0),
                    "multi": k.get("multi", 0),
                    "id": id
                }]
        else:
            a = random.randint(0, self.verbsList.__len__() - 1)
            temp = self.verbsList.pop(a)
            return [{"label": temp[0], "id": temp[-1]}]

    # Дополнение
    def createAddiction(self, lastWords):
        if lastWords.__len__() != 0:
            try:
                k = lastWords[lastWords.__len__() - 1][0]
                f = int(k.get("id", -1))
                ids = []
                i = 2048
                while (i > 1):
                    if f >= i:
                        ids.append(int(i))
                        f -= i
                    i /= 2
                # print(ids)
                newIDs = []
                a = random.randint(0, 1)
                if a == 0:
                    a = random.randint(0, ids.__len__() - 1)
                    newIDs.append(ids.pop(a))
                a = random.randint(0, ids.__len__() - 1)
                newIDs.append(ids.pop(a))
                newIDs.sort()
                # print(newIDs)
            except BaseException:
                newIDs = [2]
            ans = []
            for u in newIDs:
                # if u == 2:
                #     em = []
                #     ans.append(self.createVerb(em))

                if u == 4:
                    al = ["с конем", "с кем-то", "со мной", "с тобой", "с ним", "с ней"]
                    a = random.randint(0, al.__len__() - 1)
                    if a > 1:
                        if (lastWords[-2][0].get("type", -1) == 1):
                            t_face = lastWords[-2][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        elif (lastWords[-3][0].get("type", -1) == 1):
                            t_face = lastWords[-3][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al = al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        else:
                            pass
                    else:
                        ans.append([{"label": al[a]}])
                elif u == 8:
                    al = ["коню", "кому-то", "мне", "тебе", "ему", "ей"]
                    a = random.randint(0, al.__len__() - 1)
                    if a > 1:
                        if (lastWords[-2][0].get("type", -1) == 1):
                            t_face = lastWords[-2][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        elif (lastWords[-3][0].get("type", -1) == 1):
                            t_face = lastWords[-3][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al = al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        else:
                            pass
                    else:
                        ans.append([{"label": al[a]}])
                elif u == 16:
                    al = ["коня", "кого-то", "меня", "тебя", "его", "её"]
                    a = random.randint(0, al.__len__() - 1)
                    if a > 1:
                        if (lastWords[-2][0].get("type", -1) == 1):
                            t_face = lastWords[-2][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        elif (lastWords[-3][0].get("type", -1) == 1):
                            t_face = lastWords[-3][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al = al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        else:
                            pass
                    else:
                        ans.append([{"label": al[a]}])
                elif u == 32:
                    al = ["о коне", "о ком-то", "о мне", "о тебе", "о нём", "о ней"]
                    a = random.randint(0, al.__len__() - 1)
                    if a > 1:
                        if (lastWords[-2][0].get("type", -1) == 1):
                            t_face = lastWords[-2][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        elif (lastWords[-3][0].get("type", -1) == 1):
                            t_face = lastWords[-3][0].get("face", -1)
                            al = al[2:]
                            if t_face == -1:
                                pass
                            elif t_face == 0:
                                al = al[1:]
                            elif t_face == 1:
                                al = al.pop(1)
                            elif t_face == 2:
                                al = al[:2]
                            a = random.randint(0, al.__len__() - 1)
                            ans.append([{"label": al[a]}])
                        else:
                            pass
                    else:
                        ans.append([{"label": al[a]}])
                elif u == 64:
                    al = ["в ульпан", "домой", "в квартиру", "в банк", "туда"]
                    a = random.randint(0, al.__len__() - 1)
                    ans.append([{"label": al[a]}])
                elif u == 128:
                    al = ["в ульпане", "дома", "в квартире", "в банке", "там"]
                    a = random.randint(0, al.__len__() - 1)
                    ans.append([{"label": al[a]}])

            if ans.__len__() != 0:
                return ans
        return [{
            "label": "test"
        }]

    def createAdverb(self):
        al = ["и", "а", "но", "потому что", "чтобы", "тогда"]
        al = [{"label": "и"},
              {"label": "а"},
              {"label": "но"},
              {"label": "потому что"},
              {"label": "чтобы", "time": 1},
            {"label": "тогда", "time": 1}]
        a = random.randint(0, al.__len__() - 1)
        return [al[a]]