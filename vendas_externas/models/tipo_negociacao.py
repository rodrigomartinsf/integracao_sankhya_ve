from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class TipoNegociacaoModel(Base):

  __tablename__ = 'tipo_negociacao'

  id_forma_pagamento_sankhya   = Column(Integer, primary_key = True)
  id_forma_pagamento_ve        = Column(Integer)
  id_condicao_pagamento_ve     = Column(Integer)
  forma_pag_desc               = Column(String(200))
  cond_pag_desc                = Column(String(200))

  def __init__(self,id_forma_pagamento_sankhya=None, id_forma_pagamento_ve=None, id_condicao_pagamento_ve=None, forma_pag_desc=None, cond_pag_desc=None):
    self.id_forma_pagamento_sankhya = id_forma_pagamento_sankhya
    self.id_forma_pagamento_ve      = id_forma_pagamento_ve
    self.id_condicao_pagamento_ve   = id_condicao_pagamento_ve
    self.forma_pag_desc             = forma_pag_desc
    self.cond_pag_desc              = cond_pag_desc

  def getIdFormaPagamentoSankhya(self):
    return self.id_forma_pagamento_sankhya

  def getIdFormaPagamentoVe(self):
    return self.id_forma_pagamento_ve
  
  def getIdCondicaoPagamentoVe(self):
    return self.id_condicao_pagamento_ve

  def setIdFormaPagamentoSankhya(self, new):
    self.id_forma_pagamento_sankhya = new
  
  def setIdFormaPagamentoVe(self, new):
    self.id_forma_pagamento_ve = new
  
  def setIdCondicaoPagamentoVe(self, new):
    self.id_condicao_pagamento_ve = new
