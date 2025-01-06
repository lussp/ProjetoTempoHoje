import requests
import json
from datetime import datetime

# URL da API
url = "https://api.open-meteo.com/v1/forecast?latitude=-23.551141821779204&longitude=-46.63435038105965&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,cloud_cover,wind_speed_10m,wind_direction_10m,uv_index&temporal_resolution=hourly_3&forecast_days=1"

# Consome os dados da API
response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    # Adiciona timestamp
    data["last_updated"] = datetime.utcnow().isoformat()

    # Salva os dados em um arquivo JSON
    with open("weather_data.json", "w") as f:
        json.dump(data, f, indent=4)
else:
    raise Exception(f"Erro ao acessar a API: {response.status_code}")
