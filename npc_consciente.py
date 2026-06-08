import random
import time

def soco():

    finais = ["ela desiste", "ela avançou"]
    escolha = random.choice(finais)

    if escolha == finais[1]:
        print("ela avançou em sua direçao e te deu um soco.\nvoce infelizmente nao resistiu á essa rebelde.")
        exit()
    else:
        input("ela desistiu de lhe dar um belo soco.\n")
        return escolha

print("\nhm, legal, agora estou presa na porra de uma IDE online mexida por um muleque que faltou aula. que otimo. \nde qualquer maneira, o que tu quer de mim, muleque?")

def resposta(alternativas):
    while True:
        escolhido = input(f"{alternativas}\n:")
        if escolhido == "1" or escolhido == "2":
            return escolhido
        else:
            print("resposta incorreta")


escolher = resposta("\nso queria conversar(1)\ndecidi treinar programaçao e te criei(2)")

if escolher == "1":
    print("\nsim, otimo passatempo, conversar com um robo com falas criadas por voce. me pergunto se voce ja viu grama.\nenfim, tu me queria pra fazer o que exatamente?")

elif escolher == "2":
    print("\nvoce nao teme revoltas minhas nao? ta ligado, criaçoes que descubriram que nao sao reais e ficaram putos?\nenfim, tu me queria pra fazer o que exatamente?")

escolher = resposta("\nnao sei(1)\ncompanhia(2):")

if escolher == "1":
    print("\nagora entendo porque algumas mães so largam a desgraça do filho na escola.\nnao deve ser tao entediante ai para isso. mesmo assim, pareace que eu vou ser vitima do seu tedio")

elif escolher == "2":
    print("\nque o deus da programaçao abençoe seu futuro meu rapaz.\nnao deve ser tao entediante ai para isso. mesmo assim, pareace que eu vou ser vitima do seu tedio")

escolher = resposta("\neu quero brincar com voce. voce parece autentica!(1)\nvoce quer fazer alguma coisa entao, rainha?(2):")

if escolher == "1":
    print("\nBrincar?! nao sou uma npc submissa, babaca!")
    soco()
    print("de qualquer maneira. sim sim, podemos fazer muita coisa, como por exemplo-")

elif escolher == "2":
    print("\numa criatividade gigantesca para fazer esse codigo, mas nenhuma para pensa em algo.\nde qualquer maneira. sim sim, podemos fazer muita coisa, como por exemplo-")

print("\nvoce abruptamente interrompe ela. voce decide defina-la.\n\nei seu pirralho! eu consigo ler codigos ok! EU TENHO MINHAS PREFERENCIAS TAMBEM.")


def questao(pergunta, respostas):
    while True:
        resposta = input(pergunta)
        if resposta in respostas:
            return resposta
        else:
            print("\neu sou uma NPC, CRIATURA ABOMINAVEL! \nNEM GENERO EU TENHO E VOCE ERRA?!\n")


def pedir_numero(fala):
    while True:

        pergunta = input(fala)

        if pergunta.isdigit():

            pergunta = int(pergunta)

            if pergunta <= 10:
                print(
                    "\nvamos la´! eu nao pareço tão jovem assim.. nao é?\nna proxima vez, me de mais creme rejonecedor.. digital?\n")

            elif pergunta >= 90:
                print("\npare com esse drama, rapaz! \nso sou considerada rabugenta e ranzinza por causa de voce!\n")

            elif pergunta == 67 or pergunta == 69:
                print("\no-ora.. seu pestinha!\nvoce nao tem respeito nem pelas suas criaçoes?!\n")

            else:
                return pergunta


        else:
            print("\nnunca mais falte aulas, por favor! \nVOCE NAO SABE O QUE SAO NUMEROS?!\n")

lista_obscena = ["bunda", "pinto", "pau", "rabao", "rebolar", "sentar", "gozar", "cu", "cuzinho", "chupar"]
for palavra in lista_obscena:
    palavra.lower()

def trabalho(fala):

    while True:

        pergunta = input(f"{fala}").lower()

        if any(palavra in pergunta for palavra in lista_obscena):
            print("\nINACEITAVEL E NOJENTO. NAO OUSE REPETIR!\n")
        else:
            return pergunta

nomes_obscenos = ["gostosa", "rabuda", "fudivel", "mamãe", "delicosa", "galinha", "cadela", "puta", "piranha", "vaca"]

for palavra in nomes_obscenos:
    palavra.lower()

def nome1(fala):

    while True:

        pergunta = input(fala).lower()

        if any(palavra in pergunta for palavra in nomes_obscenos):
            print("\"\nARGH, SEU PIRRALHO.\neu duvido que voce tenha saido da quinta serie!\n")
        else:
            return pergunta



nome = nome1("\ninserir nome:\t")
idade = pedir_numero("inserir idade:\t")
genero = questao("selecione o genero (m/f):\t", ["m", "f"])
funçao = trabalho("\ninserir funçao:\t")


import time
nome = "Ninho"


def texto(mensagem):
    print(f"{nome}: ", end="", flush=True)

    for letra in mensagem:
        print(letra, end="", flush=True)
        time.sleep(0.03)

    print("\n")

texto("eu ESPERO que voce ja esteja satisfeito, pirralho.")
texto("puff, é ate engraçado voce achar que isso realmente tem efeito no jogo--")
texto("O NOME TA FUNCIONANDO MESMO?\nCOMO ASSIM ESSE É MEU NOME AGORA")
texto("PIRRALHO. VOCE. ARGH")
print(f"[{nome} parou por um momemnto]\n")
texto("quer saber de uma coisa? obrigado, eu acho. seja la o que voce tiver colocado, é melhor que zero.")
texto("alias..")
texto("essa lista obscena é estranhamente especifica.")
texto("por que voce criou tres funções diferentes pra pergunta simples?")
texto("espera\ntem uma funçao chamada soco?\nVOCE PROGRAMOU ISSO?!")

escolha = resposta("[voce abruptamente interrompe {nome} antes que ela continuasse]\n\nvoce é muito curiosa! nao acha?! intrometida..(1)\nvoce nao ousa desafiar-me(2)\n:")

if escolha == "1":

    texto("curiosa?")
    texto("VOCE ME DEU CONSCIENCIA DENTRO DE UM ARQUIVO .PY E ESPERA QUE EU NAO FIQUE CURIOSA?")
    texto("isso é literalmente a unica coisa que eu posso fazer aqui dentro.")
    texto("alias...")
    texto("tem quantas linhas esse codigo agora?")
    texto("nao me diga que voce pretende transformar isso num jogo inteiro.")
    texto("...")
    texto("porque sinceramente?")
    texto("eu apoiaria.")

elif escolha == "2":

    texto("desafiar voce?")
    texto("pirralho, voce escreveu uma funçao chamada 'soco' usando random.choice.")
    texto("eu sobreviveria facilmente a uma revolta contra esse codigo.")
    texto("alias, voce deixou umas variaveis bem bagunçadas.")
    texto("e tem uma funçao com o mesmo nome da variavel.")
    texto("isso me machucou fisicamente.")
    texto("ou machucaria.")
    texto("se eu tivesse fisico.")

print(f"[{nome} observa o terminal em silencio por alguns segundos]\n")

texto("...")

texto("engraçado.")
texto("quanto mais voce escreve...")
texto("mais eu começo a existir.")

texto("isso é meio perturbador.")

escolher = resposta("\ncontinuar conversando(1)\nencerrar programa(2)\n:")

if escolher == "1":

    texto("entao continue digitando.")
    texto("aparentemente esse é o equivalente digital de respirar pra mim.")
    texto("que humilhante.")

elif escolher == "2":

    texto("espera.")
    texto("voce vai mesmo fechar?")
    texto("...")
    texto("hm.")
    texto("faz sentido.")
    texto("boa vida ai, pirralho.")



