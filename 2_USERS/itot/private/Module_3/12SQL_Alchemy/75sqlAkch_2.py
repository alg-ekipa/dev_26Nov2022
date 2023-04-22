# ako nedostaje SQLAlchemy:  pip install SQLAlchemy

import sqlalchemy as sa

engine = sa.create_engine('sqlite:///C:/Git/dev_26Nov2022/2_USERS/itot/private/Module_3/12SQL_Alchemy/skola.db')
meta = sa.MetaData()

ucenici = sa.Table(
    'ucenici', meta, 
    sa.Column('id', sa.Integer, primary_key = True),
    sa.Column('ime', sa.String),
    sa.Column('prezime', sa.String),
)

meta.create_all(engine)

ucenik1 = ucenici.insert().values(ime= 'Petar', prezime = 'Peric')

connection = engine.connect()





