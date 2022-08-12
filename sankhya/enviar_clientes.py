from classes.auth import Auth
from classes.cliente_service import ClienteService
from classes.cidade_service import CidadeService
from classes.cliente import Cliente
from classes.database import Session


session = Session()

auth = Auth()
jsessionid = auth.logon()

clientes = ClienteService(jsessionid)

for row in clientes.getAll().items():

  cidade = CidadeService(jsessionid, row[1]['cidade'], row[1]['bairro'])
  cid = cidade.searchCidadeByCodigo()
  bairro = cidade.searchBairroByCodigo()
  print(bairro)
  cliente = Cliente(row[1]['codigo_parceiro'], row[1]['razao_social'], row[1]['nome_parceiro'], row[1]['tipo_pessoa'], row[1]['cgc_cpf'], 
                    row[1]['inscricao_estadual'], row[1]['data_nascimento'], row[1]['rota'], row[1]['prazo'], row[1]['cep'], row[1]['complemento'], 
                    bairro['descricao'], cid['descricao'], cid['estado'], row[1]['tabela_preco'])
  session.add(cliente)
  session.commit()
  session.close()

  
auth.logout()