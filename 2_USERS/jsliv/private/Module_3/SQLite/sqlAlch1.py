import sqlalchemy as db

#Umetanje podataka u tablicu

engine = db.create_engine("sqlite:///skola.db")
meta = db.MetaData()

ucenici =db.Table(
    "ucenici", meta,
    db.Column("id", db.Integer, primary_key=True),
    db.Column("ime", db.String),
    db.Column("prezime", db.String)
)

ucenik1 = ucenici.insert().values(ime= "Petar", prezime = "Perić")


