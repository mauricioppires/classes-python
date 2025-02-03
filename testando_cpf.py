from classes.cpf import Cpf

#
# NOTA: Os dados inseridos aqui, 
# sao gerados automaticamente por:
# 4devs.com.br/gerador_de_cpf
#

lst_cpf = ['432.971.058-79', 
           '678.797.041-24', 
           '013.617.825-10', 
           '12345678900', 
           44444444444, 
           '77777777777', 
           '12345']

for n in lst_cpf:
    print('-'*80)
    cpf = Cpf(n)
    print(f"CPF: {cpf}")
    print(f"Formato: {cpf.formato()}")
    print(f"Validação: {'Válido' if cpf.validar() else 'Inválido'}")
    print(f"UF: {cpf.uf()}")
print('-'*80)
