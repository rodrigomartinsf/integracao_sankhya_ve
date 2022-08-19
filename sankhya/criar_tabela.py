from classes.auth import Auth
from classes.cliente_service import ClienteService
from classes.cidade_service import CidadeService
from models.cliente import ClienteModel
from classes.database import Session
from sqlalchemy.orm import declarative_base
from classes.database import engine  

session = Session()

cliente = ClienteModel()
cliente.createTable()
