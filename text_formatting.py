def remove_brackets(somestring):
    stringlist = [char for char in somestring]
    goodlist = []
    score = 0
    for element in stringlist:
        if element == '{' or element == '(' or element == '[':
            score -= 1
        elif element == '}' or element == ')' or element == ']':
            score += 1
        elif score >= 0:
            goodlist.append(element)
    
    return ''.join(goodlist)


def one_sentence(somestring):
    stringlist = [char for char in somestring]
    goodlist = []
    for element in stringlist:
    #! I know this is stupid
        if element == '.':
            break
        else:
            goodlist.append(element)
    return ''.join(goodlist)