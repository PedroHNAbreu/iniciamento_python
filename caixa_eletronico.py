import time

def fala_dramatica(mensagem, tempo:float, quebra_linha="s"):
    for palavra in mensagem:
        print(palavra, end="", flush=True)
        time.sleep(tempo)

    if quebra_linha == "s":
        print("\n")

def aviso(mensagem="\n\tERROR", seriedade="nula"):
    if mensagem != "\n\tERROR":
        print(f"\n\t{mensagem.upper()}", end="")
    else:
        print(mensagem)

    if seriedade == "boa":
        print("✅")
    elif seriedade == "ruim":
        print("⚠️")
    elif seriedade == "nula":
        print("\n")
    else:
        print(seriedade)
            

def numero(mensagem="insira um numero"):

    while True:
        pergunta = input(mensagem)
        try:
            if pergunta.startswith("-"):
                aviso("sem numeros negativos", "ruim")
            else:
                pergunta = float(pergunta)
                if pergunta.is_integer():
                    return int(pergunta)
                else:
                    return pergunta
        except ValueError:
            aviso("valor invalido", "ruim")


def especifica(mensagem, *alternativas):
    while True:
        pergunta = input(mensagem).upper()
        if pergunta not in alternativas:
            aviso("error", "ruim")
        else:
            return pergunta

        
#LEMBRETE, QUEBRA DE LINHA NATURAL COM ALT+Z
rodando = True
saldo = 1000

while rodando:
    menu = especifica("\n[ V ] Veja o saldo\n[ D ] Deposite uma quantia.\n[ S ] Saque uma quantia\n[ E ] Encerre o programa\n>", "E", "V", "D", "S", "s", "d", "v", "e") #nao consegui deixar o input inicial no .lower().

    if menu == "V" or menu == "v":
        aviso(f"seu saldo é {saldo}$", "👝")

    elif menu == "D" or menu == "d":
        depositar = numero("\ninsira quantia que queira depositar, abaixo.\n[o maximo que voce pode depositar é valor maximo do seu saldo]\n\n>")
        if depositar > saldo:
            aviso("depositaçao maior que saldo", "ruim")
        elif depositar == 0:
            aviso("numero nulo", "ruim")
        else:
            saldo += depositar
            aviso("depositaçao concluida", "boa")

    elif menu == "S" or menu == "s":
        sacar = numero("\ninsira a quantia que queira sacar, abaixo.\n\n>")

        if sacar > saldo:
            aviso("saque maior que saldo", "ruim")
        elif sacar == 0:
            aviso("numero nulo", "ruim")
        else:
            saldo -= sacar
            aviso("saque concluido", "boa")

    elif menu == "E" or menu == "e":

        print("\n", end="")
        fala_dramatica("encerrando programa", 0.08, "n")
        fala_dramatica("...", 1, "n")
        rodando = False