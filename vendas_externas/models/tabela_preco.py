from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class TabelaPrecoModel(Base):

  __tablename__ = 'tabela_preco'

  id_tabela_preco_sankhya   = Column(Integer, primary_key = True)
  id_tabela_preco_ve        = Column(Integer)
  tabela_preco_desc         = Column(String(50))

  def __init__(self,id_tabela_preco_sankhya=None, id_tabela_preco_ve=None, tabela_preco_desc=None):
    self.id_tabela_preco_sankhya = id_tabela_preco_sankhya
    self.id_tabela_preco_ve      = id_tabela_preco_ve
    self.tabela_preco_desc       = tabela_preco_desc

  def getIdTabelaPrecoSankhya(self):
    return self.id_tabela_preco_sankhya

  def getIdTabelaPrecoVe(self):
    return self.id_tabela_preco_ve
  
  def getTabelaPrecoDesc(self):
    return self.tabela_preco_desc

  def setIdTabelaPrecoSankhya(self, new):
    self.id_tabela_preco_sankhya = new
  
  def setIdTabelaPrecoVe(self, new):
    self.id_tabela_preco_ve = new
  
  def setTabelaPrecoDesc(self, new):
    self.tabela_preco_desc = new
