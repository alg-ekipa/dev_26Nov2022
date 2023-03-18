import datetime as dt
from dateutil.relativedelta import relativedelta, FR
from dateutil import tz

sadašnji_trenutak = dt.datetime.now()
neki_datum = dt.datetime (2020, 10, 5, 12, 0, 0)

print ('Sadašnji trenutak:', sadašnji_trenutak)
print ('Neki datum:', neki_datum)

print ('Razlika između ta dva datuma/trenutka: ', sadašnji_trenutak-neki_datum)