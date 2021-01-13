import wmi
import win32gui as win32
import pandas as pd
from pywinauto import Desktop

# Czytanie z pliku csv będącego templatką dla danych w programie
df = pd.read_csv('temp.csv')

# Inicjalnizacja stringa ktory uzyty do zamienienia tablicy nazw procesow w jednego stringa
process_string = " "

# Zmienna windows przechowuje wszytskie otawrte okna w systemie -> windows jest lista
windows = Desktop(backend="uia").windows()

# Zamiana listy windows na jednego stringa
process_string = process_string.join( w.window_text() for w in windows)

# Okno na którym aktualnie skupiony jest kursor
w = win32.GetWindowText(win32.GetForegroundWindow())

# Funckja sprawdzająca czy dane słowo zawiera sie w stringu -> w przypadku programu czy nazwa procesu zawiera sie na liscie
def containsWord(s, w):
    return f' {w} ' in f' {s} '


# Dodawania czasu do aktywności okna jeśli jest otwarte oraz dodawanie czasu używania tego okna jeśli kursor jest na nim skupiony
for index, row in df.iterrows():
    if(containsWord(process_string,row['Name'])):
        df.at[index,'Time Active'] += 2
        if(containsWord(w,row['Name'])):
            df.at[index,'Time Focused'] += 2


print(df)


