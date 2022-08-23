import sqlalchemy
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine('mysql+pymysql://root@localhost:3306/integracao?charset=utf8mb4', echo=True)
Session = sessionmaker(bind=engine)


