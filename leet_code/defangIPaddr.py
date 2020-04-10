# replaces '.' in IP address with '[.]'
def defangIPaddr(address):
    print(address)
    newAddy = ''
    for x in address:
        if x == '.':
            x = '[.]'
        newAddy=newAddy+x
    print(newAddy)
    return newAddy

address='1.1.1.1'
defangIPaddr(address)
