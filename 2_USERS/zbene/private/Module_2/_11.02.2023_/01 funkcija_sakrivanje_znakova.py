#521478523691234

def maskirni_broj (znakovi):
    if znakovi == '-':
        print ('Maskirni znakovi: ', znakovi)
    else: '#' * (len (znakovi)-4) + znakovi [-4:]
znakovi = input ('Unesi sve znakove kreditne kartice: ')
print ('Maskirni znakovi: ', maskirni_broj(znakovi))

#3698-521-47852

