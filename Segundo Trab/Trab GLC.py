def parenteses_balanceados(expr):
    pilha = []
    for c in expr:
        if c == '(':
            pilha.append('(')
        elif c == ')':
            if not pilha or pilha.pop() != '(':
                return False
    return not pilha

def reconhecer_expressao(expr):
    simbolos_validos = {'x', 'y', '(', ')', '<', '>'}
    if not all(c in simbolos_validos for c in expr):
        return False
    return parenteses_balanceados(expr)

def reconhecer_comando(cmd):
    cmd = cmd.strip()

    if cmd.startswith("repita"):
        partes = cmd[len("repita"):].split("ate")
        if len(partes) != 2:
            return False
        corpo, expr = partes
        return reconhecer_comando(corpo.strip()) and reconhecer_expressao(expr.strip())

    elif cmd.startswith("{") and cmd.endswith("}"):
        bloco = cmd[1:-1].strip()
        comandos = [c.strip() for c in bloco.split(";")]
        return all(reconhecer_comando(c) for c in comandos)

    else:
        return all(c in {'a', 'b'} for c in cmd)
exemplos = [
    "aab",                               
    "{a; b; ab}",                        
    "repita a ate (x)",                 
    "repita {a; b} ate ((x)y)",         
    "repita a ate ((x>y)<)",            
    "repita a ate ((x>y)"               
]

for ex in exemplos:
    print(f"{ex} -> {'valido' if reconhecer_comando(ex) else 'invalido'}")
