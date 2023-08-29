from CONSTANT import CSVLINK
from pathlib import Path
import csv 


# write new numbers to csv file
def writeToCSV(fileName,newMembers):
    write(fileName,newMembers)

# get uniqe members
def uniqeMembers(fileName,newMembers):
    teleFile = fileName+"TeleMobile"
    numbersCSV = read(teleFile) # remove all existing number in TeleMobile file
    setCSVNumbers = set(numbersCSV)
    setNewMembers = set(newMembers)
    setResult = setNewMembers - setCSVNumbers

    teleFile = fileName+"NotTeleMobile"
    numbersCSV = read(teleFile)
    setCSVNumbers = set(numbersCSV)
    result = list(setResult - setCSVNumbers) # remove all existing number in NotTeleMobile file

    return result


# write to csv
def write(fileName,numbers):
    fileLink = CSVLINK + fileName + ".csv"
    with open(fileLink, "a") as csvfile:
        csvwriter = csv.writer(csvfile,lineterminator='\n')
        for x in numbers:
            csvwriter.writerow([x])

        csvfile.close()


# read from csv
def read(fileName):
    numbers = []
    fileLink = CSVLINK + fileName + ".csv"
    # Create File if not exist
    file1 = Path(fileLink)
    file1.touch(exist_ok=True)
    with open(fileLink, "r") as csvfile:
        csvreader = csv.reader(csvfile,lineterminator='\n')
        for row in csvreader:
            numbers.append(row[0])

        csvfile.close()

    return numbers

def checkSameValueCSV(name):
    teleFile = name + "NotTeleMobile"
    num = read(teleFile)

    seen = set()
    for x in num:
        if x not in seen:
            seen.add(x)
    print("len csv: "+len(num))
    print("------------------------")
    print("len uniq" + len(seen))


# print(read("IranTeleMobile"))
