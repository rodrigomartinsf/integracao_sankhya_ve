from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class RotaModel(Base):

  __tablename__ = 'rotas'

  id_rota_sankhya   = Column(Integer, primary_key = True)
  id_rota_ve        = Column(Integer)
  rota_desc         = Column(String(50))

  def __init__(self,id_rota_sankhya=None, id_rota_ve=None, rota_desc=None):
    self.id_rota_sankhya = id_rota_sankhya
    self.id_rota_ve      = id_rota_ve
    self.rota_desc       = rota_desc

  def getIdRotaSankhya(self):
    return self.id_rota_sankhya

  def getIdRotaVe(self):
    return self.id_rota_ve
  
  def getRotaDesc(self):
    return self.rota_desc

  def setIdRotaSankhya(self, new):
    self.id_rota_sankhya = new
  
  def setIdRotaVe(self, new):
    self.id_rota_ve = new
  
  def setRotaDesc(self, new):
    self.rota_desc = new
