import csv
from math import sqrt
#path = 'empresas_estagiarios.csv'
path = 'profissionais_conteudo.csv'
def loadCSV():
    file = open(path, newline='')
    reader = csv.reader(file)
    header = next(reader)
    header.remove('')
    data=[]
    for line in reader:
        item = {
            "Empresa": "",
            "Avaliacoes": []
        }

        for index, valor in enumerate(line):
            if index == 0:
                # Primeiro item da lista = nome da empresa
                item["Empresa"] = valor
            else:
                # Demais itens = avaliacao de usuario
                """
                Como o nome do usuario ta no header, na mesma sequencia
                em que os itens são acessados, basta passar o index - 1,
                para saber de quem foi a nota
                """
                if(valor != ""):
                    item["Avaliacoes"].append({
                        header[index - 1]: (valor)
                    })

        data.append(item)
    return (data)

def trans_dic(data):
    for emp in data:
        #users[emp['Empresa']] = emp['Avaliacoes']
        di=[]
        for j in emp['Avaliacoes']:
            for chave in j.keys():
                #chave = fruta
                valor = j[chave]
                if (chave != "Profissao"):
                    di.append(float(valor))
                else:
                    di.append(valor)
        users[emp['Empresa']] = di
    return users


data = loadCSV()
users = {}
users = trans_dic(data)
#print(recommend('ALIANCA EQUIPAMENTOS CONTEINERES DE MANAUS', users))
#print(users)