from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Chaves de API seguras via variáveis de ambiente
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
SHEETS_API_KEY = os.getenv('SHEETS_API_KEY')
SHEET_ID = '1pyEiDyOdNIQ3rdv-4M_WL3kIU0DMVgc2INu16M9ggA4'
SHEET_RANGE = 'teste!A1:D31'

@app.route('/weather')
def get_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Porto,PT&appid={WEATHER_API_KEY}&units=metric'
    res = requests.get(url)
    return jsonify(res.json())

@app.route('/sheet-data')
def get_sheet_data():
    url = f'https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{SHEET_RANGE}?key={SHEETS_API_KEY}'
    res = requests.get(url)
    return jsonify(res.json())

if __name__ == '__main__':
    app.run()