from classes.auth import Auth
from models.cliente import ClienteModel
from classes.cliente_service import ClienteService
from classes.database import Session
from sqlalchemy.future import select
from typing import List

class App:

  def __init__(self):
    self.session = Session()
    self.auth = Auth()
    self.token_acesso = self.auth.logon()

  def start(self):
    self.insert()
    self.session.close()

  def getClientesFromDatabase(self):
    query = select(ClienteModel)
    result = self.session.execute(query)
    clientes_model: List[ClienteModel] = result.scalars().all()
    return clientes_model

  def insert(self):
    clientes_model = self.getClientesFromDatabase()
    for cliente in clientes_model:
      cliente_service = ClienteService(cliente.getCgcCpf(), self.token_acesso)
      cliente_existe = cliente_service.verificaCliente()
      if cliente_existe:
        # Atualiza
        cliente_service.update(cliente)
      else:
        #Cadastra Novo
        id_cliente = cliente_service.insert(cliente)
        #Atualiza o codigo do VE no banco de dados Paralelo
        cliente.setCodigoVe(id_cliente)
        self.session.commit()

