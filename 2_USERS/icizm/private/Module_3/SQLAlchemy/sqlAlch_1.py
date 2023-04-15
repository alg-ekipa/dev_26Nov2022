import sqlalchemy as db 

engine = db.create_engine('sqlite:///skola.db') # tu radimo sa SQLiteom ali ne direktno sa njim
meta = db.MetaData()

ucenici = db.Table(
    'ucenici', meta, 
    db.Column('id', db.Integer, primary_key = True),
    db.Column('ime', db.String), 
    db.Column('prezime', db.String)
)

meta.create_all(engine)
