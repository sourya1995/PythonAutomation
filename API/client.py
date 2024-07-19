import requests
from ssl import SSLError, SSLCertVerificationError
import json

class Client(object):
    def __init__(self, url: str, ssl_verify=True, cert_path=None):
        self.url = url
        if cert_path:
            self.ssl_verify = cert_path
        else:
            self.ssl_verify = ssl_verify

    def get(self) ->  str:
        body = requests.get(self.url, verify=self.ssl_verify).content
        return json.loads(body) #JSON string to dictionary
    

if __name__ == "__main__":
    client  = Client('https://api.met.no/weatherapi/airqualityforecast/0.1/stations')
    stations = client.get()
    print("Name of the first station :" + stations[0].get('name')) #return the name of the first station