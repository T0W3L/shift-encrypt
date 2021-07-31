def shift(s,n):
    return ''.join(chr(ord(char) - n) for char in s)

def deshift(s,n):
    return ''.join(chr(ord(char) + n) for char in s)
'''
Functions use ord() to get integer of character, shifts/deshifts it,
then turns it back into string using chr()
Uses ''.join to add spaces as it iterates through characters
'''

def shiftencrypt(filename,n):
    '''
    Reads file, shifts n times, adds 'LOCKED', writes to file.
    '''  
    with open(filename,'r') as file:
        text = file.read()
    ## read file

    lockedtext = shift(text,n)
    ## shift text

    with open(filename,'w') as file:
        file.write(lockedtext)
        file.write('LOCKED')
    ## writes to file, adds 'LOCKED' to end


def shiftdecrypt(filename,n):
    '''
    Reads file, removes 'LOCKED', deshifts n times, writes to file.
    '''    
    with open(filename,'r') as file:
        text = file.read()
        text = text.removesuffix('LOCKED')
    ## reads file and removes 'LOCKED' suffix
    
    unlockedtext = deshift(text,n)
    ## deshift text

    with open(filename,'w') as file:
        file.write(unlockedtext)
    ## write deshifted text into file


def main(filename,n):
    '''
    Looks for suffix 'LOCKED' and shifts/deshifts accordingly
    '''
    with open(filename,'r') as file:
        text = file.read()
    ## read file

    if(text.endswith('LOCKED')):
        shiftdecrypt(filename,n)
    else:
        shiftencrypt(filename,n)
    ## look for 'LOCKED' suffix and shift/deshift accordingly


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='File Encrypter [SHIFT]')
    parser.add_argument('file', help='File to encrypt/decrypt.')
    parser.add_argument('-k', '--key', type=int, default=1)
    parser.add_argument('-a', '--auto', action='store_true',
    help='Auto Encrypt/Decrypt.')
    parser.add_argument('-e', '--encrypt', action='store_true',
    help='Encrypt file.')
    parser.add_argument('-d', '--decrypt', action='store_true',
    help='Decrypt file.')

    args = parser.parse_args()
    
    file = args.file
    key = args.key
    auto = args.auto
    encrypt = args.encrypt
    decrypt = args.decrypt

    if (auto and encrypt) or (encrypt and decrypt) or (decrypt and auto):
        raise TypeError('Please specify only ONE option (-a/-e/-d).')
    elif auto:
        print('Running AUTO with KEY: ' + str(key) + '...')
        main(file, key)
    elif encrypt:
        print('Running ENCRYPT with KEY: ' + str(key) + '...')
        shiftencrypt(file, key)
    elif decrypt:
        print('Running DECRYPT with KEY: ' + str(key) + '...')
        shiftdecrypt(file, key)