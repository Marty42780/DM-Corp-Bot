def russianTranslate(entree):
    listfr = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    listru = ['A', 'a', 'Б', 'b', 'б', 'c', 'Д', 'д', 'E', 'e', 'F', 'f', 'Г', 'г', 'H', 'h', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'M', 'м', 'Н', 'н', 'О', 'o', 'П', 'п', 'Q', 'q', 'Р', 'р', 'S', 's', 'T', 't', 'У', 'у', 'B', 'в', 'W', 'w', 'X', 'x', 'Y', 'y', 'З', 'з']
    output = ""
    if 'Ja' in entree:
        entree = entree.replace('Ja', 'Я')
    if 'ja' in entree:
        entree = entree.replace('ja', 'я')
    if 'JA' in entree:
        entree = entree.replace('JA', 'Я')
    if 'Ju' in entree:
        entree = entree.replace('Ju', 'Ю')
    if 'ju' in entree:
        entree = entree.replace('ju', 'ю')
    if 'JU' in entree:
        entree = entree.replace('ju', 'Ю')
    for letter in entree:
        if not letter in listfr:
            output = output + (letter)
            # print('pas trouvé : ' + letter)
        else:
            output = output + (listru[listfr.index(letter)])    
    
    return(output)


def roleFinder(ctx, x):
    '''Retourne le role demandé

    Arguments:
        ctx {} -- [description]
        x {int} -- identifiant du role voir ci-dessus
    '''