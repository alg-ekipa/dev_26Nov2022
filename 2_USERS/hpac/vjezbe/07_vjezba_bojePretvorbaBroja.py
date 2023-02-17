print('Unesi šifru boje: ')
R = input('R= ')
G = input('G= ')
B = input('B= ') 

bin_R = int(R,16)
bin_G = int(G,16)
bin_B = int(B,16)

print(f'Boja u heksa kodu {R}-{G}-{B} u dekadskom sutavu je {bin_R}-{bin_G}-{bin_B}')

