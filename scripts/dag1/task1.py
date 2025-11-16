import datetime as datetime
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, Boolean, Float, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
Base = declarative_base()

SQLALCHEMY_DATABASE_URI = f"postgresql://test_user1:dactil_1981@195.133.13.173:5432/test1"

engine=sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(bind=engine)


Session_local = sessionmaker(autocommit=False, autoflush=False,  bind=engine)
session_local = Session_local()

class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    currency = Column(String(length=50), nullable=False)
    value = Column(Float, nullable=False)
    currate_date = Column(TIMESTAMP, nullable=False, index=True)

new_record = Currency(
              currency = 'EUR',
              value=10.101,
              currate_date = datetime.datetime.now()
              )

new_record2 = Currency(
              currency = 'RUB',
              value=20.202,
              currate_date = datetime.datetime.now()
              )

session_local.add(new_record)
session_local.add(new_record2)
session_local.commit()