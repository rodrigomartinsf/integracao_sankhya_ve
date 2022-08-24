import requests
import json
import os

class Auth:

  user: str
  password: str
  token_acesso: str
  token_renovacao: str
  url: str
  header: str

  def __init__(self, user=None, password=None, token_acesso=None, token_renovacao=None, url=None):
    self.user = os.environ.get('VE_USER')
    self.password = os.environ.get('VE_PASSWORD')
    self.token_acesso = token_acesso
    self.token_renovacao = token_renovacao
    self.url = os.environ.get('VE_URL_LOGIN')
    
  def getTokenAcesso(self):
    return self.token_acesso

  def getTokenRenovacao(self):
    return self.token_renovacao

  def getUrl(self):
    return self.url

  def getUser(self):
    return self.user

  def getPassword(self):
    return self.password

  def setTokenAcesso(self, new):
    self.token_acesso = new
  
  def setTokenRenovacao(self, new):
    self.token_renovacao = new

  def logon(self):
    session = requests.Session()
    session.auth = (self.getUser(), self.getPassword())
    response = session.post(self.getUrl())
    aDict = json.loads(response.text)
    self.setTokenAcesso(aDict['token_acesso'])
    self.setTokenRenovacao(aDict['token_renovacao'])
    return aDict['token_acesso']



