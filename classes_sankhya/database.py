import sqlalchemy
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine('sqlite:///integracao.db', echo=True)
Session = sessionmaker(bind=engine)
