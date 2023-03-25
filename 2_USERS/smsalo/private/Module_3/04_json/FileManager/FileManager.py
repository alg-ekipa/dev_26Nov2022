'''
    MODUL               Modul 3 - Programiranje u Pythonu
    TEMA                Rad s datotekama
    NASLOV              File Manager - Primjer za txt datoteku, 
                        Dodati i za json i csv
'''

import os

def isFilePathExists(filePath):
    '''
    Metoda koja vraća True ili False, ovisno o tome je li "filePath" postoji ili ne
    '''
    return os.path.exists(filePath)


def openFilePathForReading(filePath):
    '''
    Metoda za otvaranje konekcije prema datoteci navedenoj u "filePath" varijabli
    Konekcija prema datoeci će biti otvorena za čitanje
    '''
    if not isFilePathExists(filePath):
        return f'Datoteka {filePath} ne postoji!'
    
    try:
        fileReader = open(filePath, 'r')
        return fileReader
    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja otvaranja {filePath} datoteke za citanje!'


def openFilePathForWriting(filePath):
    '''
    Metoda za otvaranje konekcije prema datoteci navedenoj u "filePath" varijabli
    Konekcija prema datoeci će biti otvorena za pisanje
    '''
    try:
        fileWriter = open(filePath, 'r')
        return fileWriter
    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja otvaranja {filePath} datoteke za pisanje!'


def writeToFilePathOpenClose(filePath, content):
    '''
    Metoda za pisanje u datoteku navedenu u "filePath" varijabli
    Koristi 'w' opciju za pisanje u datoteku.
    Sadržaj zapisa se nalazi u varijabli 'content'
    '''
    try:
        with open(filePath, 'w') as fileWriter:
            fileWriter.write(content)
    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja pisanja u {filePath} datoteku!'


def writeLineWithFileWriter(lineWriter, lineContent):
    '''
    Metoda za pisanje linije pomoću konekcije navedene u "lineWriter" varijabli
    Koristi 'w' opciju za pisanje u datoteku.
    Sadržaj zapisa se nalazi u varijabli 'content'
    '''
    try:
        lineContent = lineContent + '\n'
        lineWriter.write(lineContent)

    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja pisanja linije pomoću {lineWriter} konekcije!'


def readFromFilePathOpenClose(filePath):
    '''
    Metoda za čitanje iz datoteke navedene u "filePath" varijabli
    Koristi 'r' opciju za čitanje iz datoteke.
    '''
    if not isFilePathExists(filePath):
        return f'Datoteka {filePath} ne postoji!'

    try:
        with open(filePath, 'r') as fileReader:
            return fileReader.read()
    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja čitanja iz {filePath} datoteke!'


def readLineWithFileReader(lineReader):
    '''
    Metoda za čitanje linije iz konekcije navedene u "fileReader" varijabli
    Koristi 'r' opciju za čitanje iz datoteka.
    '''
    try:
        line = lineReader.readLine()

        if line.endswith('\n'):
            line = line.rstrip('\n')

        return line

    except Exception as ex:
        return f'Dogodila se greska prilikom pokusaja čitanja linije pomoću {lineReader} konekcije!'


def closeFileConnection(fileConnection):
    '''
    Metoda za zatvaranje konekcije prema datoteci. Naziv konekcije je naveden u "fileConnection" varijabli
    '''
    fileConnection.close()