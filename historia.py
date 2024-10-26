import random

def gerar_introducao():
    introducoes = ["Na cidade de Nova York", "Em nova York", "Na cidade mais famosa do mundo"]
    return random.choice(introducoes)

def gerar_desenvolvimento():
    desenvolvimento = ["o nosso amigo Spider-man", "o amigão da vizinhança", " o espetacular Homem-aranha"]
    return random.choice(desenvolvimento)

def gerar_final():
    finais = ["se balançava por ai", "enfrentava vilões" ,"tentava conciliar o trabalho com a vida de heroi"]
    return random.choice(finais)

def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao}",{desenvolvimento},{final}
    return historia

if __name__ == "__main__":
     print(gerar_historia())