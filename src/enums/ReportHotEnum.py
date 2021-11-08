from enum import Enum

class REPORT_ENUM(Enum):

    # -> Campos no banco de dados:
    ID = 'CD_REPORT'
    NOME_EMPRE = 'NOME_EMPRE'
    NUMERO_EMPRE = 'ENDERECO_EMPRE'
    EDENRECO = 'NUMERO_EMPRE'
    DONO = 'DONO_EMPRE'
    GRAVIDADE = 'GRAVIDADE'
    TIPO_DANO = 'TIPO_DANO'
    TIPO_AGRO = 'CD_AGRO'
    QT_AGRO = 'QT_AGRO'
    NOME_AGRO = 'NOME_AGRO'

    # -> TAG's de template
    TAG_ID_RELATORIO = '{'+'ID_RELATÓRIO'+'}'
    TAG_NOME_FUNC = '{'+'FUNC_NOME'+'}'
    TAG_FILTRO = '{'+'FILTRO'+'}'

    TAG_NOME_EMPRE = '{'+'NOME_EMPRE'+'}'
    TAG_NUMERO_EMPRE = '{'+'NUMERO_EMPRE'+'}'
    TAG_ENDERECO = '{'+'ENDERECO'+'}'
    TAG_DONO_EMPRESA = '{'+'DONO_EMPRESA'+'}'
    TAG_NOME_AGRO = '{'+'NOME_AGRO'+'}'
    TAG_TIPO_AGRO = '{'+'CD_AGRO'+'}'
    TAG_DESC_AGRO = '{'+'DS_AGRO'+'}'
    TAG_EFEITO_ORAL = '{'+'EFEITO_ORAL'+'}'
    TAG_EFEITO_DERM = '{'+'EFEITO_DERMICO'+'}'
    TAG_EFEITO_INAL = '{'+'EFEITO_INALAR'+'}'
    TAG_QT_AGRO = '{'+'QT_AGRO'+'}'
    TAG_GRAVIDADE = '{'+'GRAVIDADE'+'}'
    TAG_TIPO_DANO = '{'+'TIPO_DANO'+'}'