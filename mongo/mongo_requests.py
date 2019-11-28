from pymongo import MongoClient
import csv

# element_base_dict = {'Jordan': 0, 'Kazuo': 0, 'Hendria': 0, 'Cassio': 0, 'Paulo': 0, 'Andressa': 0}
#
# users = {'Arthur': {'Jordan': 5, 'Kazuo': 3, 'Hendria': 5, 'Cassio': 2},
#          'Rafael': {'Jordan': 2, 'Kazuo': 5, 'Cassio': 1},
#          'Gabrielle': {'Jordan': 4, 'Hendria': 4, 'Kazuo': 3, 'Paulo': 2, 'Andressa': 5},
#          'Frederico': {'Jordan': 1, 'Kazuo': 5, 'Hendria': 3},
#          'Bruna': {'Jordan': 5, 'Hendria': 2, 'Cassio': 4},
#          'Thiago': {'Kazuo': 2, 'Hendria': 4, 'Cassio': 3},
#          'José': {'Kazuo': 3, 'Hendria': 3, 'Cassio': 4},
#          'Daniel': {'Jordan': 5, 'Kazuo': 1, 'Hendria': 5, 'Cassio': 5},
#          'Victor': {'Hendria': 3, 'Cassio': 1},
#          'Novato': {'Hendria': 2}
#          }


def load_csv(path):
    file = open(path, newline='')
    reader = csv.reader(file)
    header = next(reader)
    header.remove('')
    data = []
    for line in reader:
        item = {
            "evaluator": "",
            "evaluations": []
        }

        for index, valor in enumerate(line):
            if index == 0:
                # Primeiro item da lista = nome do filme
                item["evaluator"] = str(valor).strip().lower()
                item["evaluations"] = {}
            else:
                # Demais itens = avaliacao de usuario
                """
                Como o nome do usuario ta no header, na mesma sequencia
                em que os itens são acessados, basta passar o index - 1,
                para saber de quem foi a nota
                """
                if valor != '':
                    item["evaluations"][str(header[index - 1]).strip().lower()] = int(valor)

        data.append(item)
    return data


def populate_database(path_dataset, service, is_company=False):


    data = load_csv(path_dataset)
    client = MongoClient('mongodb://localhost:27017/')
    db = client.employes_evaluations

    if is_company:
        collection= db[service+'_company']
    else:
        collection = db[service]
    for element in data:
        collection.insert_one(element)


def register(username, password):
    pass


def login (username,password):
    return True


def populate():

    path = "empresas_estagiarios.csv"
    path_1 =  "estagiarios.csv"
    path_2 = "profissionais_conteudo.csv"
    populate_database(path_1, 'ios_testing', True)
    populate_database(path, 'ios_testing')
    populate_database(path_2, 'ios_classify')


def evaluate (username, service, evaluation_elment, point, is_company=False):

    client = MongoClient('mongodb://localhost:27017/')
    db = client.employes_evaluations
    username = str(username)
    evaluation_elment = str(evaluation_elment)

    if is_company:
        collection = db[service + '_company']
    else:
        collection = db[service]
    print(collection)
    evaluator = collection.find_one({"evaluator": username})
    user_evaluations = False
    if evaluator:
        user_evaluations = evaluator['evaluations']

    if evaluation_elment not in user_evaluations:
        try:
            user_evaluations[evaluation_elment] = point
            collection.update_one({"evaluator": username}, {'$set': {'evaluations': user_evaluations}})
        except Exception as ex:
            return False
    else:
        return False
    return True


def get_all_services():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.employes_evaluations
    collection_names = db.list_collection_names()
    services = []
    for element in collection_names:
        if str(element).find('_company') == -1:
            services.append(element)
    return services


def mount_users(service,  is_company=False):
    client = MongoClient('mongodb://localhost:27017/')
    db = client.employes_evaluations
    if is_company:
        collection = db[service + '_company']
    else:
        collection = db[service]

    all_elements = collection.find({})
    users_dict = {}

    for element in all_elements:

       users_dict[element["evaluator"]] = element["evaluations"]

    return users_dict


def mount_element_base_dict(service,  is_company=False):

    client = MongoClient('mongodb://localhost:27017/')
    db = client.employes_evaluations
    if is_company:
        collection = db[service + '_company']
    else:
        collection = db[service]
    all_elements = collection.find({})
    all_options = []
    for element in all_elements:
        for evaluted_element in element['evaluations']:
            all_options.append(evaluted_element)
    all_options = sorted(set(all_options))
    element_base_dict = {}
    for option in all_options:
        element_base_dict[option] = 0

    return element_base_dict


# print(evaluate("carolinne de souza", "ios_testing", "yago kaic", 5, is_company=True))
# users_dict = mount_users("ios_testing",True)
# element_base_dict = mount_element_base_dict("ios_testing", True)
# print(element_base_dict)
populate()