import requests
import json

class CidadeService:

  def __init__(self, jsessionid,codigo_cidade, codigo_bairro):
    jsession = 'JSESSIONID='+jsessionid
    self.headers = {'Cookie': jsession}
    self.url = "http://navecunha.nuvemdatacom.com.br:9665/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json"
    self.codigo_cidade = codigo_cidade
    self.codigo_bairro = codigo_bairro

  def getHeaders(self):
    return self.headers
  
  def getUrl(self):
    return self.url

  def getCodigoCidade(self):
    return self.codigo_cidade

  def getCodigoBairro(self):
    return self.codigo_bairro

  def searchCidadeByCodigo(self):
    body = {
            "serviceName": "CRUDServiceProvider.loadRecords",
            "requestBody": {
              "dataSet": {
                "rootEntity": "Cidade",
                "includePresentationFields": "S",
                "offsetPage": "0",
                "criteria": {
                  "expression": {
                    "$": "this.CODCID = " + self.getCodigoCidade() 
                  }
                },
                "entity": {
                  "fieldset": {
                    "list": "NOMECID,UF"
                  }
                }
              }
            }
          }
    r = requests.get(self.getUrl(), data=json.dumps(body), headers=self.getHeaders())
    aDict = json.loads(r.text)
    cidade = aDict['responseBody']['entities'].get('entity',None)
    if cidade is None:
      return {'cidade': None, 'estado': None}
    else:
      cidade = {'descricao': cidade['f0']['$'], 'estado': cidade['f3']['$']}
      return cidade

  def searchBairroByCodigo(self):
    body = {
            "serviceName": "CRUDServiceProvider.loadRecords",
            "requestBody": {
              "dataSet": {
                "rootEntity": "Bairro",
                "includePresentationFields": "N",
                "offsetPage": "0",
                "criteria": {
                  "expression": {
                    "$": "this.CODBAI = " + self.getCodigoBairro() 
                  }
                },
                "entity": {
                  "fieldset": {
                    "list": "CODBAI,NOMEBAI"
                  }
                }
              }
            }
          }
    r = requests.get(self.getUrl(), data=json.dumps(body), headers=self.getHeaders())
    aDict = json.loads(r.text)
    bairro = aDict['responseBody']['entities'].get('entity',None)
    if bairro is None:
      return {'descricao': None}
    else:
      bairro = {'descricao': bairro['f1']['$']}
    return bairro

    