from classes.auth import Auth
from classes.cliente_service import ClienteService
from classes.cidade_service import CidadeService
from classes.cliente import Cliente
from classes.database import Session


session = Session()

cliente = Cliente()
cliente.createTable()