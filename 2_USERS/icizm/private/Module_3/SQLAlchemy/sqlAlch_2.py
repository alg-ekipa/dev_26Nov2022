import sqlalchemy as db 

# Umetanje podataka u prethodno stvorenu tablicu

engine = db.create_engine('sqlite:///skola.db') 
meta = db.MetaData()

ucenici = db.Table(
    'ucenici', meta, 
    db.Column('id', db.Integer, primary_key = True),
    db.Column('ime', db.String), 
    db.Column('prezime', db.String)
)

meta.create_all(engine)

ucenik1 = ucenici.insert().values(ime = 'Petar', prezime = 'Petričović') # sad bi on to trebao prebaciti u bazu ali NE IDE

connection = engine.connect()

connection.execute(ucenik1)