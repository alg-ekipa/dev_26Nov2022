a = int(input('Unesi prvi broj: '))
b = int(input('Unesi drugi broj: '))

while b == 0:
    print('Unesite drugi broj koji je različit od 0!!!')
    b = int(input('Unesi drugi broj: '))

zbroj = a + b
razlika = a - b
umnožak = a * b
količnik = a / b
potencija = a ** b
modulo = a % b

print(f'Unešeni su brojevi {a} i {b}:\n\nnjihov zbroj je {a} + {b} = {zbroj}\
      \nnjihova razlika je {a} - {b} = {razlika}\
      \nnjihov umnožak je {a} * {b} = {umnožak}\
      \nnjihov količnik je {a} / {b} = {količnik}\
      \nnjihova potencija je {a} ** {b} = {potencija}\
      \nnjihov modulo je {a} % {b} = {modulo}')