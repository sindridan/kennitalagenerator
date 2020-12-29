from random import randint

#býr til kt, hunsar datetime check,
def genKT(annum):
    day = randint(1,31)
    if day < 10:
        day = "0" + str(day)
    day = str(day)
    
    month = randint(1,12)
    if month < 10:
        month = "0" + str(month)
    month = str(month)
    
    annum = str(annum)
    year = annum[-2:]
    
    seveneight = str(randint(20,99))
    
    if int(annum[:2]) < 20:
        era = "9"
    else:
        era = "0"
    
    firsteight = day+month+year+seveneight
    
    vartalDigits = [3,2,7,6,5,4,3,2]
    vartalSum = 0
    vartal = 0
    
    incr = 0
    for x in firsteight:
        digit = int(vartalDigits[incr]) * int(x)
        vartalSum += digit
    
    vartal = vartalSum % 11
    if vartal != 0:
        vartal = 11 - vartal
    
    
    kennitala = firsteight + str(vartal) + era
    return kennitala


# notaðu ártal sem færibreytu
kt = genKT(2020)
print(kt)
    
    