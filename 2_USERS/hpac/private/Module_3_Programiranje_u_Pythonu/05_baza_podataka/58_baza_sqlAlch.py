import sqlalchemy as db

# KREIRANJE BAZE I TABLICE 

engine = db.create_engine('sqlite:///C:/Users/office10.UCIONE/Desktop/hp/dev_26Nov2022/2_USERS/hpac/private/Module_3_Programiranje_u_Pythonu/05_baza_podataka/skola.db')
meta = db.MetaData()

ucenici = db.Table(
    'ucenici', meta,
    db.Column('id', db.Integer, primary_key = True),
    db.Column('ime', db.String),
    db.Column('prezime', db.String)
)

meta.create_all(engine)
