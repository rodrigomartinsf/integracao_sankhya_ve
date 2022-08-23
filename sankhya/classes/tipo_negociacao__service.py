import requests
import json

class TipoNegociacaoService:

  def __init__(self, jsessionid,codigo_parceiro):
    jsession = 'JSESSIONID='+jsessionid
    self.headers = {'Cookie': jsession}
    self.url = "http://navecunha.nuvemdatacom.com.br:9665/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json"
    self.codigo_parceiro = codigo_parceiro

  def getHeaders(self):
    return self.headers
  
  def getUrl(self):
    return self.url

  def getCodigoParceiro(self):
    return self.codigo_parceiro

  def searchTipoNegociacaoByCodigoParceiro(self):
    body = {
            "serviceName": "CRUDServiceProvider.loadRecords",
            "requestBody": {
              "dataSet": {
                "rootEntity": "ComplementoParc",
                "includePresentationFields": "N",
                "offsetPage": "0",
                "criteria": {
                  "expression": {
                    "$": "this.CODPARC = " + self.getCodigoParceiro()
                  }
                },
                "entity": {
                  "fieldset": {
                    "list": "SUGTIPNEGSAID"
                  }
                }
              }
            }
          }
    r = requests.get(self.getUrl(), data=json.dumps(body), headers=self.getHeaders())
    aDict = json.loads(r.text)
    complemento = aDict['responseBody']['entities'].get('entity',None)
    if complemento is None:
      return {'codigo': None}
    else:
      complemento = {'codigo': complemento['f0']['$']}
      return complemento