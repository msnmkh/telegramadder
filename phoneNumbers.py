# import module
import random
from CONSTANT import COUNTRIES
from readWrite import uniqeMembers

# format: (N)(xxx)(xxx)(xxxx)
def createPhoneNumbers(country,limit):
    numbers = []
    if(country == "1"): #India
        numbers = IndiaMobileNumber(limit)
    elif(country == "2"): #Russia
        numbers = RussiaMobileNumber(limit)
    elif(country == "3"): #US
        numbers = USMobileNumber(limit)
    elif(country == "4"): #Indonesia
        numbers = IndonesiaMobileNumber(limit)
    elif(country == "5"): #Brazil
        numbers = BrazilMobileNumber(limit)
    elif(country == "6"): #Egypt
        numbers = EgyptMobileNumber(limit)
    elif(country == "7"): #Turkey
        numbers = TurkeyMobileNumber(limit)
    elif(country == "8"): #Iran
        numbers = IranMobileNumber(limit)
    elif(country == "9"): #France
        numbers = FranceMobileNumber(limit)        

    newNumber = uniqeMembers(COUNTRIES[country]["Name"],numbers)
    return newNumber


# Create France mobile numbers with virtual number
# "+33 7or6 xx xx xx xx.
def FranceMobileNumber(limit):
    phoneCode = COUNTRIES['9']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = random.choice(["7","6"]) # 900-999
        second = ""
        for i in range(8):
            second += str(random.randint(0,9))
        num = phoneCode + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)

    return numbers

# Create Turkey mobile numbers with virtual number
# "+90-n-xxx-xxxx " n=>500-549
def TurkeyMobileNumber(limit):
    phoneCode = COUNTRIES['7']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = str(random.randint(500,549)) # 500-549
        second = ""
        for i in range(7):
            second += str(random.randint(0,9))
        num = phoneCode + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)

    return numbers


# Create Egypt mobile numbers with virtual number
# "+20-n-xxxx-xxxx " n=>10,11,12,15
def EgyptMobileNumber(limit):
    phoneCode = COUNTRIES['6']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = random.choice(["10","11","12","15"]) # 900-999
        second = ""
        for i in range(8):
            second += str(random.randint(0,9))
        num = phoneCode + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)

    return numbers

# Create Brazil mobile numbers with virtual number
# "+55 n-9xxxx-xxxx" n=>11-99
def BrazilMobileNumber(limit):
    phoneCode = COUNTRIES['5']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = str(random.randint(11,99) )# 900-999
        second = ""
        for i in range(8):
            second += str(random.randint(0,9))
        num = phoneCode + first + "9" + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)

    return numbers

# Create Indonesia mobile numbers with virtual number
# "+62 8xx-xxxx-xxxx  
def IndonesiaMobileNumber(limit):
    phoneCode = COUNTRIES['4']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = random.choice(["811","812","813","814","815","816","817","818","819","838","852","853","855","856","858","859"]) 
        second = ""
        for i in range(8):
            second += str(random.randint(0,9))
        num = phoneCode + "8" + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)

    return numbers

# Create Russia mobile numbers with virtual number
# "+7-nnn-xxx-xx-xx" n=>900-999
def RussiaMobileNumber(limit):
    phoneCode = COUNTRIES['2']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = str(random.randint(900,999) )# 900-999
        second = ""
        for i in range(7):
            second += str(random.randint(0,9))
        num = phoneCode + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)

    return numbers

# Create India mobile numbers with virtual number
# "+91 xxxx-nnnnnn"
def IndiaMobileNumber(limit):
    phoneCode = COUNTRIES['1']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = random.choice(["7","8","9"]) # 6,7,8,9
        second = ""
        for i in range(9):
            second += str(random.randint(0,9))
        num = phoneCode + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)


    return numbers

# Create US mobile numbers with virtual number
# +1 (NXX) NXX-XXXX, where the Ns denote any of the digits 2–9, and the Xs denote any digit 0–9. 
def USMobileNumber(limit):
    phoneCode = COUNTRIES['3']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        first = random.choice(["2","3","4","5","6","7","8","9"])
        third = random.choice(["2","3","4","5","6","7","8","9"])
        second = ""
        for i in range(2):
            second += str(random.randint(0,9))
        forth = ""
        for i in range(6):
            forth += str(random.randint(0,9))
        num = phoneCode + first + second + third + forth # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)


    return numbers

# Create Iran mobile numbers
def IranMobileNumber(limit):
    phoneCode = COUNTRIES['8']['Code'] # contry code
    numberSet = set()
    cnt = 0
    while cnt < limit:
        # first = random.choice(["0","1","3"])
        first = random.choice(["1","3"])
        second = ""
        for i in range(8):
            second += str(random.randint(0,9))
        num = phoneCode + "9" + first + second # number
        numberSet.add(num)
        cnt += 1
    else:
        numbers = list(numberSet)


    return numbers

