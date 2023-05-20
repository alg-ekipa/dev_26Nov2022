from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

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


