import json
import word
import translator

t = ["хотеть", [["хочу", "хочешь", "хочет"], ["хотел", "хотела"]], [["хотим", "хотите", "хотят"], ["хотели"]], 1094]

ctrl = 1

if ctrl == 0:
    l = []
    s = input()

    kom = s.split()

    l.append(kom[0])
    l.append([])
    l.append([])
    l.append(kom[-1])

    l[1].append([])
    l[1].append([])
    l[1][0].append(kom[1])
    l[1][0].append(kom[2])
    l[1][0].append(kom[3])
    l[1][1].append(kom[4])
    l[1][1].append(kom[5])

    l[2].append([])
    l[2].append([])
    l[2][0].append(kom[6])
    l[2][0].append(kom[7])
    l[2][0].append(kom[8])
    l[2][1].append(kom[9])

    f = open("verbs.txt", 'r')
    try:
        save = json.loads(f.read())
    except BaseException:
        save = []
    f.close()
    f = open("verbs.txt", 'w')
    save.append(l)
    f.write(json.dumps(save))
    f.close()
else:
    # print(json.loads(json.dumps(l)))
    # f = open("verbs.txt", 'r')
    # print(json.loads(f.read()))
    # f.close()
    tt = translator.Translator()
    tt.match("я говорю с тобой")