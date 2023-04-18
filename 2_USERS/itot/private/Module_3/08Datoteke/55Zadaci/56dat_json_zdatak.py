
'''
1. vježbu Planer (Scheduler) prepraviti tako da umjesto inputa, podatke uzima iz datoteke korisnici.txt
 mogu se iskoristiti i neke druge vježbe, npr vozni park, računi...
'''

import datetime as dt
import locale 
locale.setlocale(locale.LC_TIME, 'hr_HR')


planer_it = {
    '010123' : [('07:17', 'Test 0101230 7:17'), ('22:17', 'Test 0101230 22:17')],
    '170423' : [],
    '161123' : [],
   }






sada_vrijeme = dt.time(12,30,0) # vrijeme kreirano preko parametara koje prenosimo 

print(sada_vrijeme)

a = dt.time(12,30,30,444445)
print(a)

dan = dt.date.weekday(danas) # vraća broj 0-6, počinje 0:ponedjeljak, 1:utorak...
print('Danas je', dan)

# formatirani ispis datume pomoću strftime - koristi objekt date
print(danas.strftime('%A'))
print(danas.strftime('%d.%m.%Y'))
print(danas.strftime('%d.%m.%y'))
print(danas.strftime('%dth %B %Y'))
print('\nHrvatski jezik:')


import json
file_path = 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/54json_example1.json'
file_write_path= 'C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/08Datoteke/54shipping_adress.txt'
trazeni_key= "shipTo" 

dict_json = {}
try:
    with open(file_path, 'r') as file_reader:
        dict_json = json.load(file_reader)
except Exception as e:
    print(f'Pogreska: {e}')

dict_adresa = dict_json[trazeni_key]   # pretvara iz rijecnika po keyu, u novi rijecnik

for x,y in dict_adresa.items():
    file_writer = open(file_write_path, "a")
    file_writer.write(f'{str(x)} {str(y)}\n')
    file_writer.close()

 
