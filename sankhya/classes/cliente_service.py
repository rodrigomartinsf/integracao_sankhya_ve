import requests
import json

class ClienteService:

  def __init__(self, jsessionid):
    self.jsession = 'JSESSIONID='+jsessionid
    self.headers = {'Cookie': self.jsession}
    self.url = "http://navecunha.nuvemdatacom.com.br:9665/mge/service.sbr?serviceName=CRUDServiceProvider.loadRecords&outputType=json"
    self.body = {"serviceName": "CRUDServiceProvider.loadRecords","requestBody": {"dataSet": {"rootEntity": "Parceiro","includePresentationFields": 
                         "N","offsetPage": "0","criteria": {"expression": {"$": "this.CLIENTE = 'S'"}},"entity": {"fieldset": {
                         "list": "CODPARC,RAZAOSOCIAL,NOMEPARC,TIPPESSOA,CGC_CPF,IDENTINSCESTAD,DTNASC,CODROTA,PRAZOPAG,CEP,COMPLEMENTO,CODBAI,CODCID,CODTAB,BLOQUEAR,ATIVO,CODEND,NUMEND,LATITUDE,LONGITUDE"}}}}}
    
  def getHeaders(self):
    return self.headers
  
  def getUrl(self):
    return self.url

  def getBody(self):
    return self.body

  def getAll(self):
    response = dict()
    i = 0
    r = requests.get(self.getUrl(), data=json.dumps(self.getBody()), headers=self.getHeaders())
    aDict = json.loads(r.text)
    clientes = aDict['responseBody']['entities']['entity']
    for row in clientes:
      response[i] = {'codigo_parceiro': row['f0']['$'], 
                     'razao_social': row['f1'].get('$',None),
                     'nome_parceiro': row['f2'].get('$',None),
                     'tipo_pessoa': row['f3'].get('$',None),
                     'cgc_cpf': row['f4'].get('$',None),
                     'inscricao_estadual': row['f5'].get('$',None),
                     'data_nascimento': row['f6'].get('$',None),
                     'rota': row['f7'].get('$',None),
                     'prazo': row['f8'].get('$',None),
                     'cep': row['f9'].get('$',None),
                     'complemento': row['f10'].get('$',None),
                     'bairro': row['f11'].get('$',None),
                     'cidade': row['f12'].get('$',None),
                     'tabela_preco': row['f13'].get('$',None),
                     'bloquear': row['f14'].get('$',None),
                     'ativo': row['f15'].get('$',None),
                     'endereco': row['f16'].get('$',None),
                     'numero': row['f17'].get('$',None),
                     'latitude': row['f18'].get('$',None),
                     'longitude': row['f19'].get('$',None)
                     }
      i += 1
    return response


  