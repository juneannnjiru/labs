upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def molecule_to_list(molecule):
    if molecule[0] not in upper: #check that molecule starts with capital letters 
        return None
    
    atom = []
    for i in range(len(molecule)):  
        symbol = molecule[i]   #Add first letter of molecule as symbol for an atom
        if molecule[i+1] in upper:
            number = 1   #default nummber of atoms for given symbol is 1 if no number follows it
            atom.append((symbol, number))

        elif molecule[i+1] in lower: 
            symbol = symbol + molecule[i+1]    #Add second letter as part of symbol for atom well if its a small letter
            if molecule[i+2] in num:        #check if followed by number
                number = int(molecule[i+2])
            else: 
                number = 1      #if not, default number is one
                atom.append((symbol, number))

    return atom
