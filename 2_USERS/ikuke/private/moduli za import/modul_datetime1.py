import datetime as dt

danas=dt.date.today() # današnji datum u obliku YYYY.MM.DD

print(danas)


sada_vrijeme=dt.time(12,30,0) # vrijeme kreirano preko parametara koje prenosimo


print (sada_vrijeme)

a=dt.time(12,30,30,444445)

print(a)

dan=dt.date.weekday(danas) #(danas #vraća broj 0-6 -- 0 , ponedjeljak, 1 - utorak)
print ("danas je", dan)

import locale
locale.setlocale(locale.LC_TIME, 'hr_HR')


print(danas)
