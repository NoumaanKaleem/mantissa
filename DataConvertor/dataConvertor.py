
#store contents from data file as a string
def readFile():

    global data
    with open('input.txt', 'r') as myfile:
        data = myfile.read()
    #    print(data)
    #    print(type(data))

def main():

    #call readfile function
    readFile()

    #set data variable to global to access in this function
    global data

    #remove first two characters from data
    data = data[2:]


    # 8 sets of characters
    n = 8
    #group string in to sets of 8 characters
    groupedData = [data[x:x+n] for x in range(0, len(data), n)]
    #remove \n from all elements
    groupedData = [i.replace('\n','') for i in groupedData]

    # loop through grouped data
    for sets in groupedData:
        # rearrange the characters in each set
        sets = sets[6:] + sets[4:6] + sets[2:4] + sets[:2]
        # convert hexadecimals to decimals
        floatValue = int(sets, 16)

        #convert decimals to binary and make sure they are 32 digits
        binaryValue = str(int(bin(floatValue)[2:]))
        zeroString = ""

        #if the binary string is less than 32 digits, add zeros in front to make it 32 digits
        if len(binaryValue) < 32:
            for x in range(32 - len(binaryValue)):
                zeroString += "0"
            binaryValue = ""
            binaryValue = zeroString + str(int(bin(floatValue)[2:]))

        #intializing variables for sign, exponent, and mantissa
        sign = int(binaryValue[:1])
        finalExponentBinary = binaryValue[1:9]
        mantissa = binaryValue[9:]

        # converting exponent binary to decimal
        Exponent1 = 0
        finalExponentBinaryList = list(finalExponentBinary)
        for i in range(len(finalExponentBinaryList)):
            digit = finalExponentBinaryList.pop()
            if digit == '1':
                Exponent1 = Exponent1 + pow(2, i)

        #exponent is equal to exponent subtract 127
        e = Exponent1 - 127

        #calculate mantissa
        mantissaExponent = 0
        for x in range(len(mantissa)):
            if mantissa[x] == "1":
                newx = x + 1
                mantissaExponent += pow(2, -newx)

        #assigning values to sign, mantissa, and exponent for final formula
        finalSign = pow(-1, sign)
        finalMantissa = 1 + mantissaExponent
        finalExponent = pow(2, e)

        #final formula which is -1^s * (1+m) * 2 ^ e
        output = finalSign * finalMantissa * finalExponent
        #display output
        print(output)

main()
