import ipfsapi

class IPFSWrapper(object):

    def __init__(self, host = '127.0.0.1', port = 5001):
        self.client = ipfsapi.Client(host, port)

    def id(self):
        return self.client.id()

    def addJsonData(self, jsonObj):
        return self.client.add_json(jsonObj)

if __name__ == "__main__":

    api = IPFSWrapper()
    
    print(api.id())
