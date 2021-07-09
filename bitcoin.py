import requests

def MakeRequest():
    search_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR API KEY',
    }

    resp = requests.get(search_url,headers=headers)

    if resp.status_code == 200:
        return Parse_Bitcoin_Info(resp.json()),resp.json()
    else:
        return None

def Parse_Bitcoin_Info(resp):
    array = resp['data']

    if array:
        precio = array[0]['quote']['USD']['price']
        formatted = '{:.2f}'.format(precio)
        print(formatted)
    else:
        print("None")

if __name__ == "__main__":
    MakeRequest()
