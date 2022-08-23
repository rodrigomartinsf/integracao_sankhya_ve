from classes.auth import Auth
from classes.cliente_service import ClienteService
from classes.cidade_service import CidadeService
from classes.endereco_service import EnderecoService
from classes.tipo_negociacao__service import TipoNegociacaoService
from models.cliente import ClienteModel
from classes.database import Session
from sqlalchemy.future import select

class App:
  
  def __init__(self):
    self.session = Session()
    self.auth = Auth()
    self.jsessionid = self.auth.logon()

  def start(self):
    self.insert()
    self.session.close()
    self.auth.logout()

  def getClientesFromApi(self):
    clientes_sankhya = ClienteService(self.jsessionid)
    return clientes_sankhya

  def insert(self):
    for row in self.getClientesFromApi().getAll().items():
      #Verifica se o cliente já esta no banco de dados
      query = select(ClienteModel).filter(ClienteModel.codigo_parceiro == row[1]['codigo_parceiro'])
      result = self.session.execute(query)
      cli = result.scalar_one_or_none()

      cidade_sankhya = CidadeService(self.jsessionid, row[1]['cidade'], row[1]['bairro'])
      cidade = cidade_sankhya.searchCidadeByCodigo()
      bairro = cidade_sankhya.searchBairroByCodigo()

      endereco_sankhya = EnderecoService(self.jsessionid, row[1]['endereco'])
      endereco = endereco_sankhya.searchEnderecoByCodigo()

      tipo_negociacao_sankhya = TipoNegociacaoService(self.jsessionid, row[1]['codigo_parceiro'])
      tipo_negociacao = tipo_negociacao_sankhya.searchTipoNegociacaoByCodigoParceiro()

      if cli:
        # Caso já tenha o cliente cadastrado faz o Update
        cli.setCodigoParceiro(row[1]['codigo_parceiro'])
        cli.setRazaoSocial(row[1]['razao_social'])
        cli.setNomeParceiro(row[1]['nome_parceiro'])
        cli.setTipoPessoa(row[1]['tipo_pessoa'])
        cli.setCgcCpf(row[1]['cgc_cpf'])
        cli.setInscricaoEstadual(row[1]['inscricao_estadual'])
        cli.setDataNascimento(row[1]['data_nascimento'])
        cli.setRota(row[1]['rota'])
        cli.setPrazo(tipo_negociacao['codigo'])
        cli.setCep(row[1]['cep'])
        cli.setEndereco(endereco['descricao'])
        cli.setNumero(row[1]['numero'])
        cli.setComplemento(row[1]['complemento'])
        cli.setBairro(bairro['descricao'])
        cli.setCidade(cidade['descricao'])
        cli.setTabelaPreco(row[1]['tabela_preco'])
        cli.setBloquear(row[1]['bloquear'])
        cli.setLatitude(row[1]['latitude'])
        cli.setLongitude(row[1]['longitude'])

        self.session.commit()
        print("cliente Atualizado!")
      else:
        # Caso contrário, Cadastra 
        cliente = ClienteModel(row[1]['codigo_parceiro'], row[1]['razao_social'], row[1]['nome_parceiro'], row[1]['tipo_pessoa'], row[1]['cgc_cpf'], 
                          row[1]['inscricao_estadual'], row[1]['data_nascimento'], row[1]['rota'], tipo_negociacao['codigo'], row[1]['cep'], endereco['descricao'], row[1]['numero'], 
                          row[1]['complemento'], bairro['descricao'], cidade['descricao'], cidade['estado'], row[1]['tabela_preco'], row[1]['bloquear'], row[1]['ativo'], 
                          row[1]['latitude'], row[1]['longitude'])
        self.session.add(cliente)
        self.session.commit()
        print("cliente cadastrado!")
    