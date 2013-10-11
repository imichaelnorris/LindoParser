import sys
import string

EQUALITY = ['=', '<=', '>=', '<', '>']

def lhs(line):
    '''move variables to left of equals sign'''
    if (not '=' in line):
        return line
    temp = line.split(' ')
    for i in EQUALITY:
        if i in temp:
            equalsLocation = temp.index(i)
    #print('equalsLocation {0}'.format(equalsLocation))
    for i in range(1, len(temp)):
        #if the intersection of a string of only numbers
        # and only numbers has length of zero, the string only contains nums
        if not len(set(temp[i]) - set(string.digits+'+'+'-')) == 0:
            #print('true')
            if ( (i-1) == equalsLocation):
                #print('eqsignloc')
                equalsLocation += 1
                temp[i], temp[i-1] = temp[i-1], temp[i]
                #print("swapped: " + temp[i-1])
                if (temp[i-1][0]) == '+':
                    temp[i-1] = temp[i-1].replace('+', '-')
                elif (temp[i-1][0] == '-'):
                    temp[i-1] = temp[i-1].replace('-', '+')
                else:
                    temp[i-1] = '-' + temp[i-1]
        else:
            pass
            #print('false')
    if (temp[-1] in ['=', '<', '<=', '>', '>=']):
        temp.append('0')
    return " ".join(temp)

def expandVariable(text, parameters):
    if (text in ['=', '<=', '>=', '>', '<']):
        temp = [text]
        for i in range(0, len(parameters)//2):
            temp *= (parameters[2*i+1] - parameters[2*i] + 1)
        return temp

    temp = [text]
    while True:
        if ('_' in temp[0]):
            pass
        else:
            break
        newtemp = []
        for equation in temp[:]:
            for i in range(parameters[0], parameters[1]+1):
                #can replace a single digit number in an equation with an index
                # _i-n, with 0<=n<=9
                try:
                    minusIndex = equation.index("_i") + 2
                    if equation[minusIndex] == '-':
                        i = i - int(equation[minusIndex + 1])
                        print("equation before: " + equation)
                        equation = equation[:minusIndex] + equation[minusIndex+2:]
                        print("equation after: " + equation)
                                            
                except IndexError:
                    pass
                newtemp.append(equation.replace('_i', str(i), 1))
        temp = newtemp
        parameters.pop(0)
        parameters.pop(0)
    return temp

def getequations(text, parameters):
    temp = text.split(' ')
    tempList = []
    for i in temp:
        tempList.append(expandVariable(i, parameters[:]))
    #print(tempList)
    output = []
    for i in range(0, len(tempList[0])):
        tempLine = []
        for j in range(0, len(tempList)):
            tempLine.append(tempList[j][i])
        output.append(" ".join(tempLine))
    print(len([lhs(i) for i in output]))
    return "\r\n".join([lhs(i) for i in output])
    
if __name__ == '__main__':
    '''text = sys.argv[1]
    parameters = [int(i) for i in sys.argv[2:]]
    print(getequations(text, parameters))'''
    pass
