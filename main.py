import time
import win32gui as win32
import pandas as pd
from pywinauto import Desktop

# Czytanie z pliku csv będącego templatką dla danych w programie
df = pd.read_csv('temp.csv')

# Funckja sprawdzająca czy dane słowo zawiera sie w stringu -> w przypadku programu czy nazwa procesu zawiera sie na liscie
def containsWord(s, w):
    return f' {w} ' in f' {s} '

# Deklaracja zmiennych używanych w dalszej cześći programu
processString = ""
windows = Desktop(backend="uia").windows()
windowFore = win32.GetWindowText(win32.GetForegroundWindow())
prevForeWindow = windowFore
processString = processString.join(w.window_text()+ " " for w in windows)
timea = time.time()
totalTime = 0

# Przy starcie
for index, row in df.iterrows():
    if(containsWord(processString,row['Name'])):
        df.at[index,'Time Active'] += 1
        if(containsWord(windowFore,row['Name'])):
            df.at[index,'Time Focused'] += 1

processString = " "
# Reszta programu
while (True):
    windowFore = win32.GetWindowText(win32.GetForegroundWindow())
    if (windowFore != prevForeWindow):
        windows = Desktop(backend="uia").windows()
        processString = processString.join(w.window_text()+" " for w in windows)
        processString += prevForeWindow
        timeDif = int(time.time() - timea)
        totalTime += timeDif
        for index, row in df.iterrows():
            if(containsWord(processString,row['Name'])):
                df.at[index,'Time Active'] += timeDif
                if(containsWord(prevForeWindow,row['Name'])):
                    df.at[index,'Time Focused'] += timeDif

        timea = time.time()
        prevForeWindow = windowFore
        processString = ""
        print(df)
        # df.to_csv('out.csv', index=False)

    time.sleep(1)

