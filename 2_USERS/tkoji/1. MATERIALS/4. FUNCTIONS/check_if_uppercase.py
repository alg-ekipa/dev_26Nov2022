def string_eval(s):
    d = {"UPPER_CASE":0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print ("Original String : ", s)
        print("No. of uppercase letters: " + str(d["UPPER_CASE"]))
        print("No. of lowercase letters: " + str(d["LOWER_CASE"]))
#        return d["LOWER_CASE"], d["UPPER_CASE"]


string_eval('Ovo je Neki teXt za TEST Pa da vidimo')