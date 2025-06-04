def verifica_tres_uns(palavra):
    estado = 'q0'

    for simbolo in palavra:
        if simbolo not in {'0', '1'}:
            return False  # caractere inválido

        if estado == 'q0':
            if simbolo == '1':
                estado = 'q1'
            elif simbolo == '0':
                estado = 'q0'
        elif estado == 'q1':
            if simbolo == '1':
                estado = 'q2'
            elif simbolo == '0':
                estado = 'q1'
        elif estado == 'q2':
            if simbolo == '1':
                estado = 'q3'
            elif simbolo == '0':
                estado = 'q2'
        elif estado == 'q3':
            if simbolo == '1':
                return False  # Quarto '1' encontrado – rejeita
            elif simbolo == '0':
                estado = 'q3'

    return estado == 'q3'


# Entrada do usuário
print("Informe uma palavra binária (composta apenas por 0 e 1).")
print("A palavra será aceita apenas se contiver EXATAMENTE três dígitos '1'.")
entrada = input("Digite a palavra: ").strip()

# Verificação e saída
if verifica_tres_uns(entrada):
    print(f"A palavra '{entrada}' foi ACEITA: contém exatamente três dígitos '1'.")
else:
    print(f"A palavra '{entrada}' foi REJEITADA: não contém exatamente três dígitos '1' ou contém caracteres inválidos.")
