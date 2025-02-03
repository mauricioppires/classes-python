"""
Nome do Arquivo: cpf.py
Autor: Mauricio P. Pires
E-mail: mauricio at portelainfo dot com dot br
Criado em: 03/02/2025
Última modificação: 03/02/2025
Descrição:
    Classe Cpf.
"""

import re

class Cpf:

  def __init__(self, documento):
    self.documento = self.limpa(documento)  # Já inicia sem caracteres inválidos

  def __str__(self):
    return self.formato()

  def limpa(self, documento):
    """ Remove caracteres não numéricos do CPF e garante que seja string. """
    return re.sub(r"[^0-9]", "", str(documento))

  def formato(self):
    """ Retorna o CPF formatado como XXX.XXX.XXX-XX, caso tenha tamanho válido. """
    if not self.tamanho():
      return "Formato Inválido"
    return f"{self.documento[:3]}.{self.documento[3:6]}.{self.documento[6:9]}-{self.documento[9:]}"

  def tamanho(self):
    """ Verifica se o CPF tem 11 dígitos. """
    return len(self.documento) == 11

  def sem_digitos_iguais(self):
    """ Retorna False se todos os dígitos forem iguais, True caso contrário. """
    return self.documento != self.documento[0] * 11

  def validar(self):
    """ Valida o CPF de acordo com a regra dos dígitos verificadores. """
    if not self.tamanho() or not self.sem_digitos_iguais():
      return False
    num = self.documento[:9]
    dvs = self.documento[9:]
    # Cálculo do primeiro dígito verificador
    soma = sum(int(p) * (10 - n) for n, p in enumerate(num))
    dv1 = 11 - (soma % 11)
    dv1 = 0 if dv1 >= 10 else dv1
    # Cálculo do segundo dígito verificador
    soma = sum(int(p) * (11 - n) for n, p in enumerate(num)) + dv1 * 2
    dv2 = 11 - (soma % 11)
    dv2 = 0 if dv2 >= 10 else dv2
    return dvs == f"{dv1}{dv2}"

  def uf(self):
    """ Retorna a unidade federativa com base no penúltimo dígito do CPF. """
    ufs = {
      1: 'DF, GO, MS, MT, TO',
      2: 'AC, AM, AP, PA, RO, RR',
      3: 'CE, MA, PI',
      4: 'AL, PB, PE, RN',
      5: 'BA, SE',
      6: 'MG',
      7: 'ES, RJ',
      8: 'SP',
      9: 'PR, SC',
      0: 'RS'
    }
    if self.tamanho():
      return ufs.get(int(self.documento[8]), "UF Inválida")
    return "UF Inválida"
