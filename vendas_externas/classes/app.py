from classes.auth import Auth
from models.cliente import ClienteModel
from models.tipo_negociacao import TipoNegociacaoModel
from models.rota import RotaModel
from models.tabela_preco import TabelaPrecoModel
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
      # Verifica se o cliente existe no VE
      cliente_service = ClienteService(cliente.getCgcCpf(), self.token_acesso)
      cliente_existe = cliente_service.verificaCliente()

      #Busca os dados do tipo de negociação do cliente
      query = select(TipoNegociacaoModel).filter(TipoNegociacaoModel.id_forma_pagamento_sankhya == cliente.getPrazo())
      result = self.session.execute(query)
      tipo_negociacao: TipoNegociacaoModel =  result.scalar_one_or_none()

      #Busca os a Rota do cliente
      query = select(RotaModel).filter(RotaModel.id_rota_sankhya == cliente.getRota())
      result = self.session.execute(query)
      rota: RotaModel =  result.scalar_one_or_none()

      #Busca a Tabela de Preço do cliente
      query = select(TabelaPrecoModel).filter(TabelaPrecoModel.id_tabela_preco_sankhya == cliente.getTabelaPreco())
      result = self.session.execute(query)
      tabela_preco: TabelaPrecoModel =  result.scalar_one_or_none()

      if cliente_existe:
        # Atualiza
        cliente_service.update(cliente, tipo_negociacao, rota, tabela_preco)
      else:
        #Cadastra Novo
        id_cliente = cliente_service.insert(cliente, tipo_negociacao, rota, tabela_preco)
        #Atualiza o codigo do VE no banco de dados Paralelo
        cliente.setCodigoVe(id_cliente)
        self.session.commit()

