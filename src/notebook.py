import requests


#For unit testing
def add_numbers(a: int, b : int) -> int:
    return a + b


#For integration test
def get_dollar_info():

    response = requests.get(f"https://mx.dolarapi.com/v1/cotizaciones/usd")
    data = response.json()
    return data["venta"]


print("Hola CI/CD en Databricks 🚀")