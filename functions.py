def separateElements(initStr):
    modStr = initStr
    finalStr = ''
    while (len(modStr) != 0):
        if (    # DOUBLE OPERATORS
                modStr[:2] == "++" or modStr[:2] == "--"):
            finalStr = finalStr + ' ' + modStr[:2] + ' '
            temp = modStr[:2]
            modStr = temp

        elif (
                # SEPARATORS
                modStr[0] == "(" or modStr[0] == ")" or modStr[0] == "{"
                or modStr[0] == "}" or modStr[0] == "[" or modStr[0] == "]"
                or modStr[0] == "," #or modStr[0] == "."
                or modStr[0] == ":"
                or modStr[0] == ";"):
            finalStr = finalStr + ' ' + modStr[0] + ' '
            temp = modStr[1:]
            modStr = temp

        elif (
                # OPERATORS
                modStr[0] == "*" or modStr[0] == "+" or modStr[0] == "-"
                or modStr[0] == "=" or modStr[0] == "/" or modStr[0] == ">"
                or modStr[0] == "<" or modStr[0] == "%"):
            finalStr = finalStr + ' ' + modStr[0] + ' '
            temp = modStr[1:]
            modStr = temp

        else:
            finalStr = finalStr + modStr[0]
            modStr = modStr[1:]
    finalStr = finalStr.strip()
    return finalStr

