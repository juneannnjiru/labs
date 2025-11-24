ATOMS = {'H':{'name':'Hydrogen', 'weight':1.00797}, 
          'He':{'name':'Helium', 'weight':4.00260},
          'C' : {'name':'Carbon', 'weight' : 12.011},
          'O' : {'name':'Oxygen', 'weight' : 15.9994} }

def molar_mass(molecule):
    mass = 0
    if molecule[0] not in ATOMS and molecule[0:2] not in ATOMS:
        return None
    else:
        for string, number in molecule:
            mass = mass + (number)*(ATOMS[string]['weight'])
        return mass

molar_mass(('H',2),('O',1))