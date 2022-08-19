from typing import Dict
import requests
import json

class ClienteService:

  def __init__(self, cgc_cpf, token_acesso):
    self.cgc_cpf = cgc_cpf
    self.token_acesso = token_acesso

  def getCgcCpf(self):
    return self.cgc_cpf

  def getTokenAcesso(self):
    return self.token_acesso

  def maskCgcCpf(self):
    cgc_cpf_to_mask = self.getCgcCpf()
    if len(self.getCgcCpf()) == 11:
      cgc_cpf = '{}.{}.{}-{}'.format(cgc_cpf_to_mask[:3], cgc_cpf_to_mask[3:6], cgc_cpf_to_mask[6:9], cgc_cpf_to_mask[9:])
    else:
      cgc_cpf = '{}.{}.{}/{}-{}'.format(cgc_cpf_to_mask[:2], cgc_cpf_to_mask[2:5], cgc_cpf_to_mask[5:8], cgc_cpf_to_mask[8:12], cgc_cpf_to_mask[12:])
    return cgc_cpf

  def verificaCliente(self):
    url = 'https://api.alkord.com/clientes?token='+ self.getTokenAcesso() +'&filtros=DOCUMENTO:ig:' + self.maskCgcCpf()
    session = requests.Session()
    response = session.get(url)
    aDict = json.loads(response.text)
    if aDict['TOTAL_REGISTROS'] < 1:
      return False
    else:
      return True

  def insert(self, cliente):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = 'https://api.alkord.com/clientes?token='+ self.getTokenAcesso()

    data = dict()
    rel = []
    data['NOME']            = cliente.getRazaoSocial()
    data['APELIDO']         = cliente.getNomeParceiro()[0:30]
    data['TIPO_PESSOA']     = cliente.getTipoPessoa()
    # Alterar TAB PREÇO 
    data['RELACIONAMENTOS'] = {'RELACIONAMENTO': 2}
    data['SITUACAO']        = 'A' if cliente.getAtivo() == 'S' else 'I' 
    data['RESTRICAO']       = ''
    data['DOCUMENTO']       = cliente.getCgcCpf()
    data['DOCUMENTO2']      = cliente.getInscricaoEstadual() if cliente.getInscricaoEstadual() is not None else 'ISENTO'
    data['INTERNET']        = ''
    data['ESTADO_CIVIL']    = 'S' 
    data['NASCIMENTO_CONSTITUICAO'] = cliente.getDataNascimento() if cliente.getDataNascimento() is not None else '2022-01-01'
    #Alterar MEIO_PAGAMENTO / CONDICAO_PAGAMENTO / ROTA (DE/PARA)
    data['COMERCIAL_VENDA'] = {'REPRESENTANTE': cliente.getRota(), 'MEIO_PAGAMENTO': 1, 'CONDICAO_PAGAMENTO': cliente.getPrazo(), 
                               'SITUACAO_CADASTRO': 1 if cliente.getAtivo() == 'S' else 3, 'PERFIL': 1, 'PERFIL_RESTRICAO': 1 if cliente.getBloquear() == 'N' else 2 }
    data['ENDERECOS']       = [{'TIPO': 'R', 'PRINCIPAL': 'S', 'CEP': cliente.getCep(), 'ENDERECO': cliente.getEndereco(), 'NUMERO': cliente.getNumero(),
                                'COMPLEMENTO': cliente.getComplemento(), 'BAIRRO': cliente.getBairro(), 'CIDADE': {'NOME': cliente.getCidade()}, 
                                'ESTADO': {'SIGLA': cliente.getEstado()}, 'PAIS': {'NOME': 'BRASIL'}, 'CAIXA_POSTAL': '', 'DESCRICAO': '', 'CONTATO_ALTERNATIVO': '',
                                'POSICIONAMENTO_LATITUDE': cliente.getLatitude(), 'POSICIONAMENTO_LONGITUDE': cliente.getLongitude()
                              }]

    data_json = json.dumps(data)
    session = requests.Session()
    response = session.post(url, data=data_json, headers=headers)
    aDict = json.loads(response.text)

    if 'REFERENCIAS' in aDict:
      return aDict['REFERENCIAS']['CODIGO']

  def update(self, cliente):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = 'https://api.alkord.com/pessoas/'+ str(cliente.getCodigoVe()) +'?token='+ self.getTokenAcesso()

    data = dict()
    data['NOME']            = cliente.getRazaoSocial()
    data['APELIDO']         = cliente.getNomeParceiro()[0:30]
    data['TIPO_PESSOA']     = cliente.getTipoPessoa()
    # Alterar TAB PREÇO 
    data['RELACIONAMENTOS'] = {'RELACIONAMENTO': 2}
    data['SITUACAO']        = 'A' if cliente.getAtivo() == 'S' else 'I' 
    data['RESTRICAO']       = ''
    data['DOCUMENTO']       = cliente.getCgcCpf()
    data['DOCUMENTO2']      = cliente.getInscricaoEstadual() if cliente.getInscricaoEstadual() is not None else 'ISENTO'
    data['INTERNET']        = ''
    data['ESTADO_CIVIL']    = 'S' 
    data['NASCIMENTO_CONSTITUICAO'] = cliente.getDataNascimento() if cliente.getDataNascimento() is not None else '2022-01-01'
    #Alterar MEIO_PAGAMENTO / CONDICAO_PAGAMENTO / ROTA (DE/PARA)
    data['COMERCIAL_VENDA'] = {'REPRESENTANTE': cliente.getRota(), 'MEIO_PAGAMENTO': 1, 'CONDICAO_PAGAMENTO': cliente.getPrazo(), 
                               'SITUACAO_CADASTRO': 1 if cliente.getAtivo() == 'S' else 3, 'PERFIL': 1 if cliente.getBloquear() == 'N' else 2, 'PERFIL_RESTRICAO': 1 }
    data['ENDERECOS']       = [{'TIPO': 'R', 'PRINCIPAL': 'S', 'CEP': cliente.getCep(), 'ENDERECO': cliente.getEndereco(), 'NUMERO': cliente.getNumero(),
                                'COMPLEMENTO': cliente.getComplemento(), 'BAIRRO': cliente.getBairro(), 'CIDADE': {'NOME': cliente.getCidade()}, 
                                'ESTADO': {'SIGLA': cliente.getEstado()}, 'PAIS': {'NOME': 'BRASIL'}, 'CAIXA_POSTAL': '', 'DESCRICAO': '', 'CONTATO_ALTERNATIVO': '',
                                'POSICIONAMENTO_LATITUDE': cliente.getLatitude(), 'POSICIONAMENTO_LONGITUDE': cliente.getLongitude()
                              }]

    data_json = json.dumps(data)
    session = requests.Session()
    response = session.put(url, data=data_json, headers=headers)
    aDict = json.loads(response.text)

    print(aDict)
    
    
  




