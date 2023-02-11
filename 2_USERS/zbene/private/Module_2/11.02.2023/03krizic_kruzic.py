ploča = [' ' for x in range (9)]

def ispis_ploče():
    red1 = ' | {} | {} | {} |'.format(ploča[0], ploča[1], ploča [2])
    red2 = ' | {} | {} | {} |'.format(ploča[3], ploča[4], ploča [5])
    red3 = ' | {} | {} | {} |'.format(ploča[6], ploča[7], ploča [8])
    print()
    print(red1)
    print(red2)
    print(red3)
    print()

ispis_ploče()

def micanje()