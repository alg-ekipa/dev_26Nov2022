import sqlalchemy as db

# umetanje podataka u tablicu



#kreiranje baze i tablice

engine=db.create_engine('sqlite:///skola.db')
meta = db.MetaData()

ucenici = db.Table(
    'ucenici', meta,
    db.Column('id', db.Integer, primary_key= True),
    db.Column('ime', db.String),
    db.Column('prezime', db.String)
)

#meta.create_all(engine)

ucenik1 = ucenici.insert()
ucenik1 = ucenici.insert().values(ime='Petar', prezime = 'Perić')

connection=engine.connect()
connection.execute(ucenik1)