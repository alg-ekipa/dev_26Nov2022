from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .tenant import Tenant


engine = create_engine('sqlite:///data/tenants.sqlite')
Session = sessionmaker(bind=engine)
session = Session()


def get_tenants(session=session):
    return session.query(Tenant).all()



def create_update_tenant(tenant):
    tenant_new = (
        session.query(Tenant)
        .filter(
            and_(
                Tenant.first_name == tenant.first_name, Tenant.last_name == tenant.last_name
            )
        )
        .one_or_none()
    )

    if tenant_new is not None:
        tenant_new.first_name = tenant.first_name
        tenant_new.last_name = tenant.last_name
        tenant_new.pin = tenant.pin
        tenant_new.is_active = tenant.is_active
    else:
        tenant_new = tenant
        session.add(tenant_new)

    session.commit()
    


def delete_tenant(tenant):
    tenant_new = (
        session.query(Tenant)
        .filter(
            and_(
                Tenant.first_name == tenant.first_name, Tenant.last_name == tenant.last_name
            )
        )
        .one_or_none()
    )

    if tenant_new is not None:
        session.delete(tenant_new)
        session.commit()