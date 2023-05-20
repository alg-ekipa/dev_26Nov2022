from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .tenant import Tenant
from .data_repo import get_tenants, create_update_tenant, delete_tenant


Base = declarative_base()

class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100))
    pin = Column(String(4))
    is_active = Column(Boolean(), default=True)

    def __repr__(self):
        return "Tenant(first_name='{self.first_name}', " \
                    "last_name='{self.last_name}', " \
                    "pin='{self.pin}', " \
                    "is_active={self.is_active})".format(self=self)



def create_tables():
    engine = create_engine('sqlite:///data/tenants.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    seed_data(session)


def seed_data(session):

        tenants = get_tenants(session)

        if len(tenants) == 0:

            tenant_pero_peric = Tenant(
                first_name = 'Pero',
                last_name = 'Peric',
                pin = '1234',
                is_active = True)
            session.add(tenant_pero_peric)

            tenant_ana_anic = Tenant(
                first_name = 'Ana',
                last_name = 'Anic',
                pin = '4321',
                is_active = False)
            session.add(tenant_ana_anic)

            tenant_marko_maric = Tenant(
                first_name = 'Marko',
                last_name = 'Maric',
                pin = '9876',
                is_active = True)
            session.add(tenant_marko_maric)

            session.commit()