

w = "E:" # путь к файлу
def dump(*lst): #lst - list of tranzaction, way - путь сохранения файла

    try:
        fp = open("Data.txt","w")
        for i in lst:
            fp.write(str(i))
    except (IOError,OSError): #oserror/ file not found
        print("An IOError has occured!")

    except  FileNotFoundError:
        print("File not found")
    finally:
        fp.flush()
        print("Ok file successfully close") #to check

def dumpWith(*lst): #lst - list of tranzaction, way - путь сохранения файла

    try:
        with open("Data1.txt","w") as f:
            for i in lst:
                f.write(str(i))
    finally:
        print("OK")
from contextlib import contextmanager
@contextmanager
def dump2(*lst):
    try:
        fp = open("Data.txt", mode='w',encoding="utf-8")
        yield fp
    except (IOError,OSError):
        print("We had an error!!!")
    except  FileNotFoundError:
        print("File not found")
    finally:
        print("Closing file", sep=' ', end='\n')
        fp.flush()
