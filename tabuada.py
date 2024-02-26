import random
import time
from getkey import key


def gerar_tabuada(operacoes: list, lower_bound: int, upper_bound: int):
    tabuada = [
        (o, i, j)
        for o in operacoes
        for i in range(lower_bound, upper_bound + 1)
        for j in range(lower_bound, upper_bound + 1)
    ]

    random.shuffle(tabuada)
    return tabuada


def operacao(operacao: str, x: int, y: int):
    if operacao in ["+", "*"]:
        oper = {"+": "+", "*": "x"}
        pergunta = f"{x} {operacao} {y} = "
        resposta = x + y if operacao in ["+"] else x * y
    elif operacao in ["-"]:
        pergunta = f"{x + y} - {y} = "
        resposta = x
    elif operacao in ["/"]:
        pergunta = f"{x * y} / y = "
        resposta = x
    else:
        raise ValueError("Operação inválida")

    return pergunta, resposta


def jogar_tabuada(operacoes: list, lower_bound: int, upper_bound: int):
    tabuada = gerar_tabuada(operacoes, lower_bound, upper_bound)
    inicio = time.time()
    corretas = 0
    erradas = 0
    repete = False

    while tabuada:
        if not repete:
            operador, min, max = tabuada.pop()
        repete = False
        pergunta, resposta = operacao(operador, min, max)
        resposta_usuario = input(pergunta)

        try:
            if resposta_usuario == "":
                interrompe_fatos = ""
                while interrompe_fatos not in ["S", "N"]:
                    fim = time.time()
                    segundos = round(fim - inicio)
                    minutos = round(segundos / 60)
                    segundos = round(segundos - 60 * minutos)
                    interrompe_fatos = str.upper(
                        input(
                            f"""Você já respondeu {corretas + erradas} questões em {minutos} minutos e {segundos} segundos.
    Deseja parar (S/N)?"""
                        )
                    )
                    print(interrompe_fatos)
                if interrompe_fatos == "S":
                    break
                else:
                    repete = True
                    continue
            elif int(resposta_usuario) == resposta:
                print("Resposta correta!\n")
                corretas += 1
            else:
                print(f"Incorreto. A resposta correta era {resposta}.\n")
                erradas += 1
                tabuada.insert(
                    0, [operador, min, max]
                )  # Coloca a conta de volta no início
        except Exception:
            print("Resposta inválida\n")
            repete = True
            continue

    fim = time.time()
    segundos = round(fim - inicio)
    minutos = round(segundos / 60)
    segundos = round(segundos - 60 * minutos)

    print(
        f"""Parabéns! Você completou a tabuada em {minutos} minutos e {segundos} segundos.
        Certas: {corretas}
        Erradas: {erradas}"""
    )


# Descomente a linha abaixo para executar o jogo
simbolo_oper = ""
operacoes = []
while simbolo_oper != "" or len(operacoes) == 0:
    if simbolo_oper not in ["+", "-", "*", "/"]:
        print("A operação deve ser +, -, x ou /\n")
    elif simbolo_oper in operacoes:
        print("Operação já cadastrada\n")
    else:
        operacoes.append(simbolo_oper)
        oper_list = ""
        for oper in operacoes:
            oper_list = f"{oper_list}{oper}, "
        print(f"\nOperações selecionadas: [{oper_list[:-2]}]\n")

    simbolo_oper = input(
        "Digite as operações que deseja (+, -, x, /)\n[ENTER] para continuar\n"
    )

    if simbolo_oper in ["x", "X"]:
        simbolo_oper = "*"


jogar_tabuada(operacoes, 1, 10)
# print(gerar_tabuada(["+", "-", "*"], 1, 10))