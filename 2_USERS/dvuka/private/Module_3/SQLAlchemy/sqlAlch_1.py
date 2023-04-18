import sqlalchemy as db

#KREIRANJE BAZE I TABLICE

engine=db.create_engine('sqlite:///C:/Users\grafika10/Desktop/dev_26Nov2022-1/2_USERS/dvuka/private/Module_3/SQLAlchemy/skola.db')
meta=db.MetaData()

ucenici=db.Table(
    'ucenici',meta,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('ime', db.String),
    db.Column('prezime', db.String)
)

meta.create_all(engine)

