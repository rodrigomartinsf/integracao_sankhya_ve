import requests
import json

class EnderecoService:

  def __init__(self, jsessionid,codigo_endereco):
    jsession = 'JSESSIONID='+jsessionid
    self.headers = {'Cookie': jsession}
    self.url = "http://navecunha.nuvemdatacom.com.br:9665/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json"
    self.codigo_endereco = codigo_endereco

  def getHeaders(self):
    return self.headers
  
  def getUrl(self):
    return self.url

  def getCodigoEndereco(self):
    return self.codigo_endereco

  def searchEnderecoByCodigo(self):
    body = {
            "serviceName": "CRUDServiceProvider.loadRecords",
            "requestBody": {
              "dataSet": {
                "rootEntity": "Endereco",
                "includePresentationFields": "S",
                "offsetPage": "0",
                "criteria": {
                  "expression": {
                    "$": "this.CODEND = " + self.getCodigoEndereco() 
                  }
                },
                "entity": {
                  "fieldset": {
                    "list": "CODEND,NOMEEND,TIPO,CODLOGRADOURO"
                  }
                }
              }
            }
          }
    r = requests.get(self.getUrl(), data=json.dumps(body), headers=self.getHeaders())
    aDict = json.loads(r.text)
    endereco = aDict['responseBody']['entities'].get('entity',None)
    if endereco is None:
      return {'descricao': None}
    else:
      endereco = {'descricao': endereco['f2']['$'] + ' ' + endereco['f1']['$']}
      return endereco

