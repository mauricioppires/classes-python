from classes.cpf import Cpf

# Exemplo de uso
for n in ['14621213067', '146.212.130-67', '12345678900', 44444444444, '77777777777', '12345']:
    print('-'*80)
    cpf = Cpf(n)
    print(f"CPF: {cpf}")
    print(f"Formato: {cpf.formato()}")
    print(f"Validação: {'Válido' if cpf.validar() else 'Inválido'}")
    print(f"UF: {cpf.uf()}")
print('-'*80)
