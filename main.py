from random import randint,uniform,sample
from time import sleep
import poems

def allRandomColor(poem):
    for verse in poem:
        newVerse = ''
        usedColor = []
        if poem.index(verse) == 0:
           color = randint(30,38)
           style = '\033[5;' + str(color) + ';0m'
           newVerse = style +'《'+ verse +'》'
        else:
            sleep(uniform(1.5,2))
            for v in verse:
                if not v == ' ':
                    while True:
                        color = randint(30,38)
                        if len(usedColor) == (len(verse)-1)/2:
                            usedColor = []
                        if color != 33 and color not in usedColor:
                            usedColor.append(color)
                            break
                style = '\033[5;'+str(color)+';0m'
                newVerse += style + v
        print(newVerse)


def randomColor(poem):
    randomVerse = poem[1]
    length = (len(randomVerse)-1)/2
    length = int(length)
    while True:
        front = sample(list(range(30, 38)), length)
        front.append(34)
        back = sample(list(range(30, 38)), length)
        lineColor = front+back
        if not 33 in lineColor:
            break
    for verse in poem:
        sleep(uniform(1.5, 2))
        newVerse = ""
        if verse == poem[0]:
            color = randint(30, 38)
            style = '\033[5;' + str(color) + ';0m'
            newVerse = style +'《'+ verse + '》'
        else:
            for v,c in zip(verse,lineColor):
                style = '\033[5;' + str(c) + ';0m'
                newVerse += style + v
        print(newVerse)




if __name__ == '__main__':
    poem = poems.xiaKeXin
    allRandomColor(poem)
    #randomColor(poem)

