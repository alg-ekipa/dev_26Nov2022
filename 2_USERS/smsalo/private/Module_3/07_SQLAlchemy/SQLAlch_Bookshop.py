import sqlalchemy as db
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#MODEL

Base = declarative_base() 

autor_izdavac = db.Table(
            "autor_izdavac",
            Base.metadata,
            db.Column("autor_id", db.Integer, db.ForeignKey("autor.id")),
            db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id"))
)

knjiga_izdavac = db.Table(
            "knjiga_izdavac",
            Base.metadata,
            db.Column("knjiga_id", db.Integer, db.ForeignKey("knjiga.id")),
            db.Column("izdavac_id", db.Integer, db.ForeignKey("izdavac.id"))
)

#tablica Autor
class Autor(Base):
    __tablename__ = "autor"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String)
    prezime = db.Column(db.String)

    #Definiramo veze između tablica/klasa
    knjige = relationship("Knjiga", backref=backref("autor"))
    izdavaci = relationship("Izdavac", secondary=autor_izdavac, back_populates="autori")

#tablica Knjiga
class Knjiga(Base):
    __tablename__ = "knjiga"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"))
    naslov = db.Column(db.String)

    #Definiramo veze između tablica/klasa
    izdavaci =relationship("Izdavac", secondary=autor_izdavac, back_populates="knjige")

#tablica Izdavac
class Izdavac(Base):
    __tablename__ = "izdavac"
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String)

    #Definiramo veze između tablica/klasa
    autori = relationship("Autor", secondary=autor_izdavac, back_populates="izdavaci")
    knjige = relationship("Knjiga", secondary=knjiga_izdavac, back_populates="izdavaci")


#FUNKCIJE I UPORABA MODELA

def get_knjige_po_izdavacu(session, ascending=True):
    '''Dohvati listu izdavaca s brojem izdanih knjiga'''
    if not isinstance(ascending, bool):
        raise ValueError(f'Vrijednost argumenta sortiranja nije ispravna: {ascending}')

    sortiraj = db.asc if ascending else db.desc

    return (
        session.query(
            #Dohvati nazive izdavaca i kreiraj novi stupac naziva "ukupno_knjiga"
            #u taj stupac dodaj vrijednost koju vrati funkcija count i naslove knjiga
            Izdavac.naziv,
            db.func.count(Knjiga.naslov).label("ukupno_knjiga")
        ).join(Izdavac.autori).group_by(Izdavac.naziv).order_by(sortiraj("ukupno_autora"))
    )

def get_autori_po_izdavacu(session, ascending=True):
    '''Dohvati listu izdavaca te broj autora čije knjige su izdali'''
    if not isinstance(ascending, bool):
        raise ValueError(f'Vrijednost argumenta sortiranja nije ispravna: {ascending}')

    sortiraj = db.asc if ascending else db.desc

    return (
        session.query(
            #Dohvati imena autora i kreiraj novi stupac naziva "ukupno_autora"
            #u taj stupac dodaj vrijednost koju vrati funkcija func.count i autore
            Izdavac.naziv,
            db.func.count(Autor.ime).label("ukupno_autora")
        ).join(Izdavac.autori).group_by(Izdavac.naziv).order_by(sortiraj("ukupno_autora"))
    )

def get_autori(session):
        '''Dohvati listu autora sortiranih po prezimenu'''
        return session.query(Autor).order_by(Autor.prezime).all()

def add_knjiga(session, ime_autora, naslov_knjige, naziv_izdavaca):
    '''Dodaje novu knjigu u bazu'''

    #Rastavljanje ime_autora na ime i prezime, dio _ nam ne treba
    ime, _, prezime = ime_autora.partition(" ")

    #Provjeri je li postoji knjiga u bazi, da izbjegnemo duple
    knjiga = (session.query(Knjiga).join(Autor).filter(Knjiga.naslov == naslov_knjige) #filter po naslovu knjie
            .filter(db.and_(Autor.ime == ime, Autor.prezime == prezime)) #filter po imenu AND prezimenu autora
            .filter(Knjiga.izdavaci.any(Izdavac.naziv == naziv_izdavaca)) #filter po nazivu izdavača
            .one_or_none()) #dohvati prvu ili ponesi na None

    #ako je gornja provjera vratila neki objekt odi u prvu if petlju i prekini funkciju
    #ako nije našla duplikat (knjiga ima vrijednost None) odi u drugu if petlju (preskoči prvu)
    if knjiga is not None:
        return

    if knjiga is None:
        knjiga = Knjiga(naslov=naslov_knjige) #Kreiraj novi objekt knjiga

    #Provjeri autora po imenu i prezimenu
    autor = (
        session.query(Autor).filter(db.and_(
                Autor.ime == ime, Autor.prezime==prezime
            )).one_or_none()
        )
    #ako nema takvog autora, kreiraj ga
    if autor is None:
            autor = Autor(ime=ime, prezime=prezime)
            session.add(autor)

        #Provjeri izdavaca
    izdavac = (
            session.query(Izdavac).filter(Izdavac.naziv == naziv_izdavaca).one_or_none()
            )
        
    #ako nema takvog izdavaca, kreiraj ga
    if izdavac is None:
            izdavac = Izdavac(naziv=naziv_izdavaca)
            session.add(izdavac)

    #Podešavanje relacija između knjige i autora i izdavaca
    knjiga.autor = autor
    knjiga.izdavaci.append(izdavac)

    session.add(knjiga)

    session.commit()

def main():
    db_engine = db.create_engine("sqlite:///bookshop.db")
    Base.metadate.create_all(db_engine)

    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    nove_knjige = [
        ["Isaac Asimov","Foundation","Random House"],
        ["Pearl Buck","The Good Earth","Random House"],
        ["Pearl Buck","The Good Earth","Simon & Schuster"],
        ["Tom Clancy","The Hunt For Red October","Berkley"],
        ["Tom Clancy","Patriot Games","Simon & Schuster"],
        ["Stephen King","It","Random House"],
        ["Stephen King","It","Penguin Random House"],
        ["Stephen King","Dead Zone","Random House"],
        ["Stephen King","The Shining","Penguin Random House"],
        ["John Le Carre","Tinker, Tailor, Soldier, Spy: A George Smiley Novel","Berkley"],
        ["Alex Michaelides","The Silent Patient","Simon & Schuster"],
        ["Carol Shaben","Into The Abyss","Simon & Schuster"]
    ]


    knjige_po_izdavacu = get_knjige_po_izdavacu(session, ascending=False)
    for row in knjige_po_izdavacu:
        print(f'Izdavac: {row.naziv}, ukupno knjiga {row.ukupno_knjiga}')

    autori_po_izdavacu = get_autori_po_izdavacu(session)
    for row in autori_po_izdavacu:
        print(f'Izdavac: {row.naziv}, ukupno knjiga {row.ukupno_autora}')

    for knjiga in nove_knjige:
        add_knjiga(session, ime_autora=knjiga[0], naslov_knjige=knjiga[1], naziv_izdavaca=knjiga[2])

    
if __name__ == "__main__":
    main()
