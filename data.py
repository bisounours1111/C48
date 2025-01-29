import os, time, json

class Data:
    def __init__(self, data_dir='data'):
        self.data_dir = data_dir + '/' + self.get_last_folder(data_dir)

    def get_last_folder(self, data_dir):
        folders = os.listdir(data_dir)
        folders.sort(key=lambda x: time.strptime(x, '%d-%m-%Y'))
        return folders[-1]

    def get_collections(self):
        return os.listdir(self.data_dir+'/collections')

    def get_collection(self, collection):
        return os.listdir(self.data_dir+'/collections/'+collection)

    def get_all_collections(self):
        collections = self.get_collections()
        data = {}
        for collection in collections:
            data[collection] = self.get_collection(collection)

        return data
    
    def get_file(self, collection, file):
        with open(self.data_dir+'/collections/'+collection+'/'+file) as f:
            return json.load(f)
            
if __name__ == '__main__':
    data = Data()
    print(data.data_dir)
    print(data.get_all_collections())