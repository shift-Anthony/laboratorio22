import requests

def ejercicio3():
    url = "https://httpbin.org/get"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        print(f"IP: {data.get('origin')}")
        print(f"Headers: {data.get('headers')}")
        print(f"Args: {data.get('args')}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    ejercicio3()