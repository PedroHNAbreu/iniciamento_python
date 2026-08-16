import json

def obter_numero(pergunta="Insira um numero\n>"):
    while True:
        numero = input(pergunta)
        try:
            if numero.startswith("-"):
                print("\nsem número negativo\n")
                
            else:
                numero = float(numero)
             
                if numero.is_integer():
                    return int(numero)
                
            
                else:
                    print("\napenas número inteiros\n")
                
        except ValueError:
            print("\nerror\n")
            
            
ficha = {}

quantidade = obter_numero("\nquantos perfis você deseja adicionar?\n\n>")
informações = obter_numero("quantos dados cada perfil terá?\n>")


for number in range(quantidade):
    chave = input("\ninsira o nome da pessoa\n>")
    ficha[chave] = {}
    for dado in range(informações):
        chave_dado = input("insira o nome do dado\n>")
        dado = input("insira o dado\n>")
        ficha[chave][chave_dado] = dado
        
        
print(ficha)


with open("cadastraçao.txt", mode="a", encoding="utf-8") as arquivo:
    # json.dump(ficha, arquivo, indent=4, ensure_ascii=False)
    arquivo.write(json.dumps(ficha, indent=4, ensure_ascii=False) + "\n")
