
def encrypt(message, shifts, alphabet):
    for letter in message:
        if letter not in alphabet:
            return None
        if len(message) != len(shifts):
            return None
    
    for number in shifts:
        if number < 0 or number >= len(alphabet):
            return None

    encrypted = ''
    for i in range(len(message)):
        j = alphabet.find('message[i]')
        encryp = alphabet[j+shifts[i]]
        encrypted += encryp 
    return encrypted
    