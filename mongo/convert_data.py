import csv
from math import sqrt
#path = 'empresas_estagiarios.csv'
#path = 'estagiarios_classify.csv'
path = 'mongo\estagiarios_classify.csv'
def loadCSV():
    file = open(path, newline='')
    reader = csv.reader(file)
    header = next(reader)
    header.remove('')
    #print("reader",reader)
    users={}
    nomes = ['x']
    linhas = []
    for line in reader:
        nomes.append(line[0].replace(" ","").upper())
        users[line[0]] = {}
        linhas.append(line)

    for line in linhas:
        for i in range(1,len(line)):
            #print(i,len(line),line[i],nomes[i])
            if(line[i] != ''):
                avaliacao = {nomes[i]:line[i]}
                users[line[0]].update(avaliacao)
    #print("nomes",nomes)
    #print("users",users)
    return (users)

def trans_dic(data):
    users = {}
    for emp in data:
        #users[emp['Empresa']] = emp['Avaliacoes']
        di=[]
        for j in emp['Avaliacoes']:
            for chave in j.keys():
                #chave = fruta
                valor = j[chave]
                if (chave != "Profissao"):
                    di.append(valor)
                else:
                    di.append(valor)
        users[emp['Empresa']] = di
    #print(users)
    return users
