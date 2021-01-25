import time
import win32gui as win32
import pandas as pd
from pywinauto import Desktop



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
            windowFore = win32.GetWindowText(win32.GetForegroundWindow())
            if (windowFore != self.prevForeWindow or int(self.totalTime/60) > self.min):
                windows = Desktop(backend="uia").windows()
                self.processString = self.processString.join(w.window_text() + " " for w in windows)
                timeDif = int(time.time() - self.timea)
                print("Czas zmiany " + str(timeDif) + " " + str(self.totalTime))
                for index, row in self.df.iterrows():
                    if (containsWord(self.processString, row['Name'])):
                        self.df.at[index, 'Time Active'] += (timeDif + 1)
                        if (containsWord(windowFore, row['Name'])):
                            self.df.at[index, 'Time Active'] += (timeDif + 1)

                self.timea = time.time()
                self.prevForeWindow = windowFore
                self.processString = ""

            if((int(self.totalTime/60)) > self.min):
                self.df.to_csv('out.csv', index=False)
                dataParse(self.main,self.df)
                self.min = self.totalTime/60

            self.totalTime += 1
            time.sleep(1)


# Funckja sprawdzająca czy dane słowo zawiera sie w stringu -> w przypadku programu czy nazwa procesu zawiera sie na liscie
def containsWord(s, w):
    return f' {w} ' in f' {s} '


def dataParse(window,dataFrame):
    print("okay parsuje")
    window.updateWindow()

