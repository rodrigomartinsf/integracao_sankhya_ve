from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date
from classes.database import engine  

Base = declarative_base()

class Cliente(Base):

  __tablename__ = 'clientes'

  id                  = Column(Integer, primary_key = True)
  codigo_parceiro     = Column(Integer)
  razao_social        = Column(String(200))
  nome_parceiro       = Column(String(200))
  tipo_pessoa         = Column(String(1))
  cgc_cpf             = Column(String(30))
  inscricao_estadual  = Column(String(30))
  data_nascimento     = Column(Date)
  rota                = Column(Integer)
  prazo               = Column(String(30))
  cep                 = Column(String(30))
  complemento         = Column(String(200))
  bairro              = Column(String(100))
  cidade              = Column(String(100))
  estado              = Column(String(2))
  tabela_preco        = Column(Integer)

  def __init__(self, codigo_parceiro=None, razao_social=None, nome_parceiro=None, tipo_pessoa=None, cgc_cpf=None, inscricao_estadual=None, data_nascimento=None, rota=None,
               prazo=None, cep=None, complemento=None, bairro=None, cidade=None, estado=None, tabela_preco=None):
    self.codigo_parceiro    = codigo_parceiro
    self.razao_social       = razao_social
    self.nome_parceiro      = nome_parceiro
    self.tipo_pessoa        = tipo_pessoa
    self.cgc_cpf            = cgc_cpf
    self.inscricao_estadual = inscricao_estadual
    self.data_nascimento    = data_nascimento
    self.rota               = rota
    self.prazo              = prazo
    self.cep                = cep
    self.complemento        = complemento
    self.bairro             = bairro
    self.cidade             = cidade
    self.estado             = estado
    self.tabela_preco       = tabela_preco

  def getCodigoParceiro(self):
    return self.codigo_parceiro

  def getRazaoSocial(self):
    return self.razao_social

  def getNomeParceiro(self):
    return self.nome_parceiro

  def getTipoPessoa(self):
    return self.tipo_pessoa

  def getCgcCpf(self):
    return self.cgc_cpf

  def getInscricaoEstadual(self):
    return self.inscricao_estadual

  def getDataNascimento(self):
    return self.data_nascimento

  def getRota(self):
    return self.rota

  def getPrazo(self):
    return self.prazo
  
  def getCep(self):
    return self.cep

  def getComplemento(self):
    return self.complemento

  def getBairro(self):
    return self.bairro

  def getCidade(self):
    return self.cidade

  def getEstado(self):
    return self.estado

  def getTabelaPreco(self):
    return self.tabela_preco

  def setCodigoParceiro(self,new):
    self.codigo_parceiro = new

  def setRazaoSocial(self,new):
    self.razao_social = new

  def setNomeParceiro(self,new):
    self.nome_parceiro = new

  def setTipoPessoa(self,new):
    self.tipo_pessoa = new

  def setCgcCpf(self,new):
    self.cgc_cpf = new

  def setInscricaoEstadual(self,new):
    self.inscricao_estadual = new

  def setDataNascimento(self,new):
    self.data_nascimento = new

  def setRota(self,new):
    self.rota = new

  def setPrazo(self,new):
    self.prazo = new

  def setCep(self,new):
    self.cep = new

  def setComplemento(self,new):
    self.complemento = new

  def setBairro(self,new):
    self.bairro = new

  def setCidade(self,new):
    self.cidade = new

  def setEstado(self,new):
    self.estado = new

  def setTabelaPreco(self,new):
    self.tabela_preco = new

  def createTable(self):
    Base.metadata.create_all(engine)
