import requests, json, os, time

def get_data(url='https://data.lillemetropole.fr/data/ogcapi/collections'):
    response = requests.get(url)
    data = response.json()
    return data

def main():
    """
    récupérer le documents principal contenant toutes les collections
    l'écrire dans un dossier dd-mm-yyyy/collections.json
    puis récupérer uniquement les collections de type 'application/json'
    les écrire dans un dossier dd-mm-yyyy/collections
    """
    ARBO = 'data/'
    data = get_data()
    date = time.strftime('%d-%m-%Y')
    os.makedirs(f'{ARBO}{date}', exist_ok=True)
    with open(f'{ARBO}{date}/collections.json', 'w') as f:
        json.dump(data, f, indent=4)

    os.makedirs(f'{ARBO}{date}/collections', exist_ok=True)
    for collection in data['collections']:
        title = collection['title']
        urls = collection['links']
        for url in urls:
            if url['type'] == 'application/json':
                file = f'{ARBO}{date}/collections/{title.split(":")[0]}/{title.split(":")[1]}.json'
                if os.path.exists(file):
                    continue
                else:
                    print(f'fetching {file}, {title=} \n {url=}')

                response = requests.get(url['href'])
                if response.status_code != 200:
                    print(f'error {response.status_code} for {url["href"]}')
                    continue
                try:
                    data = response.json()
                    os.makedirs(f'{ARBO}{date}/collections/{title.split(":")[0]}', exist_ok=True)
                    with open(f'{ARBO}{date}/collections/{title.split(":")[0]}/{title.split(":")[1]}.json', 'w') as f:
                        json.dump(data, f, indent=4)
                except Exception as e:
                    print(f'error {e} for {url["href"]}')
                    continue

if __name__ == '__main__':
    main()