import threading
import time
import win32gui as win32
import pandas as pd
from pywinauto import Desktop
from matplotlib import pyplot as plt

class Spy:
    # Czytanie z pliku csv będącego templatką dla danych w programie
    df = pd.read_csv('temp.csv')
    processString = ""
    win = Desktop(backend="uia")
    windows = Desktop(backend="uia").windows()
    windowFore = win32.GetWindowText(win32.GetForegroundWindow())
    prevForeWindow = windowFore
    processString = processString.join(w.window_text() for w in windows)
    timea = time.time()
    totalTime = 0
    min = 0
    saveTime = 20

    def __init__(self,window,*args,**kwargs):
        super(Spy, self).__init__(*args,**kwargs)
        self.main = window
        self.startSpying()

    # Przy starcie
    def startSpying(self):

        for index, row in self.df.iterrows():
            if (containsWord(self.processString,row['Name'])):
                self.df.at[index, 'Time Active'] += 1
                if (containsWord(self.windowFore, row['Name'])):
                    self.df.at[index, 'Time Focused'] += 1

        while (self.main.clock.running):
            self.windowFore = win32.GetWindowText(win32.GetForegroundWindow())
            if (self.windowFore != self.prevForeWindow or int(self.totalTime/self.saveTime) > self.min):
                windows = Desktop(backend="uia").windows()
                self.processString = self.processString.join(w.window_text() + " " for w in windows)
                timeDif = int(time.time() - self.timea)
                for index, row in self.df.iterrows():
                    if (containsWord(self.processString, row['Name'])):
                        self.df.at[index, 'Time Active'] += timeDif
                        if (containsWord(self.prevForeWindow, row['Name'])):
                            self.df.at[index, 'Time Focused'] += timeDif
                            print("i added " + str(timeDif))


                self.timea = time.time()
                self.prevForeWindow = self.windowFore
                self.processString = ""

            if((int(self.totalTime/self.saveTime)) > self.min):
                self.df.to_csv('out.csv', index=False)
                thread = threading.Thread(target=dataParse, args=(self.main,self.totalTime))
                thread.start()
                self.saveTime = 60
                self.min = self.totalTime/self.saveTime

            time.sleep(1)
            self.totalTime += 1


# Funckja sprawdzająca czy dane słowo zawiera sie w stringu -> w przypadku programu czy nazwa procesu zawiera sie na liscie
def containsWord(s, w):
    return f' {w} ' in f' {s} '


def dataParse(window,time):

    df = pd.read_csv('out.csv')
    print(df)
    sameTimes = ['YouTube', 'YouTube Music', 'Facebook', 'Messenger']
    toRemove = []
    topActiveName = []
    topActiveTime = []
    topFocusName = []
    topFocusTime = []
    diagramLabel = []
    diagramValue = []
    sum = 0
    totalTime = time
    focusPath = 'focusDiagram.png'
    activePath = 'timeStructure.png'

    for index, row in df.iterrows():
        if (row['Name'] in sameTimes):
            sameTimes[sameTimes.index(row['Name'])] = index

    for i in sameTimes:
        if (i % 2 == 0):
            df.at[i, 'Time Active'] = df.at[i, 'Time Active'] - df.at[i + 1, 'Time Active']
            df.at[i, 'Time Focused'] = df.at[i, 'Time Focused'] - df.at[i + 1, 'Time Focused']

    activeData = df.sort_values('Time Active', ascending=False).groupby('Name').head(5)[0:5]
    topActiveName = activeData['Name'].tolist()
    temp = activeData['Time Active'].tolist()
    for t in temp:
        topActiveTime.append(convertTime(t))

    activeData = df.sort_values('Time Focused', ascending=False).groupby('Name').head(5)[0:5]
    topFocusName = activeData['Name'].tolist()
    temp = activeData['Time Focused'].tolist()

    for t in temp:
        sum += t
        topFocusTime.append(convertTime(t))

    diagramLabel = topFocusName
    diagramLabel.append("Other")
    diagramValue = temp
    if((totalTime - sum)<0):
        diagramValue.append(0)
    else:
        diagramValue.append(totalTime - sum)

    plt.pie(diagramValue, labels=diagramLabel)
    plt.title("Focus Time")
    plt.tight_layout()
    plt.savefig(focusPath)
    plt.close()

    print(topActiveTime)
    print(topFocusTime)
    print(topActiveName)
    print(topFocusName)
    window.updateWindow(topFocusName,topFocusTime,topActiveName,topActiveTime,focusPath)


def convertTime(time):
    strTime = ""
    sec = 0
    min = 0
    hour = 0
    if (time >= 60):
        sec = int(time % 60)
        min = int((time / 60) % 60)
        hour = int(time / 3600)
    else:
        sec = time

    if (hour < 10):
        strTime += ("0" + str(hour) + ":")
    else:
        strTime += (str(hour) + ":")

    if (min < 10):
        strTime += ("0" + str(min) + ":")
    else:
        strTime += (str(min) + ":")

    if (sec < 10):
        strTime += ("0" + str(sec))
    else:
        strTime += str(sec)
    return (strTime)