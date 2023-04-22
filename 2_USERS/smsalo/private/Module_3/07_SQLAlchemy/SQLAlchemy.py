import sqlalchemy as db

#engine je potreban za rad s bazom
db_engine = db.create_engine('sqlite:///TvrtkaDb.db')
#kreiranje konekcije prema bazi
db_connection = db_engine.connect()
#dohvat metapodataka o bazi i tablicama
db_metadata = db.MetaData()


#dohvat podataka o tablici Employees
employees = db.Table('Employees', db_metadata, autoload= True, autoload_with=db_engine)

sql_select_upit = db.select([employees])

Result = db_connection.execute(sql_select_upit)
Result_all = Result.fetchall()
#Result_part = Result.fetchmany(1)

print(Result)

