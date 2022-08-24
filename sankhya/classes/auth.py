import requests
import json
import os

class Auth:

  usr: str
  password: str
  url_login: str
  body_login: str
  headers_login: str
  url_logout: str
  body_logout: str
  jsessionid: str

  def __init__(self):
    self.jsessionid = None
    self.user =  os.environ.get('SANKHYA_USER')
    self.password =  os.environ.get('SANKHYA_PASSWORD')
    self.url_login = os.environ.get('SANKHYA_URL_LOGIN')
    self.body_login = { "serviceName": "MobileLoginSP.login", "requestBody": { "NOMUSU": { "$": ""+ self.user +"" }, "INTERNO":{ "$":""+ self.password +"" }, "KEEPCONNECTED": { "$": "S" } } }
    self.headers_login = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    self.url_logout = os.environ.get('SANKHYA_URL_LOGOUT')
    self.body_logout = {"serviceName":"MobileLoginSP.logout","status":"1","pendingPrinting":"false"}

  def getUser(self):
    return self.user

  def getPassword(self):
    return self.password

  def getUrlLogin(self):
    return self.url_login

  def getBodyLogin(self):
    return self.body_login

  def getHeadersLogin(self):
    return self.headers_login

  def getUrlLogout(self):
    return self.url_logout

  def getBodyLogout(self):
    return self.body_logout

  def getSessionId(self):
    return self.jsessionid

  def setSessionId(self, new):
    self.jsessionid = new

  def logon(self):
    data_json = json.dumps(self.getBodyLogin())
    r = requests.post(self.getUrlLogin(), data=data_json, headers=self.getHeadersLogin())
    aDict = json.loads(r.text)
    jsessionid = aDict['responseBody']['jsessionid']['$']
    self.setSessionId(jsessionid)
    return jsessionid
    
  def logout(self):
    jsession = 'JSESSIONID='+ self.getSessionId()
    headers = {'Cookie': jsession}
    requests.post(self.getUrlLogout(), data=json.dumps(self.getBodyLogout()), headers=headers)
