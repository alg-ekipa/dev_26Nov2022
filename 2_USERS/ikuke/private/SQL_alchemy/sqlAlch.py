import sqlalchemy as db


#kreiranje baze i tablice

engine=db.create_engine('sqlite:///skola.db')
meta = db.MetaData()

ucenici = db.Table(
    'ucenici', meta,
    db.Column('id', db.Integer, primary_key= True),
    db.Column('ime', db.String),
    db.Column('prezime', db.String)
)
print 
meta.create_all(engine)

