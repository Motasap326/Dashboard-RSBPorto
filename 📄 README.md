# RSB Porto - Página com Backend Seguro

Este projeto mostra:
- Hora atual no Porto
- Clima em tempo real (via OpenWeatherMap)
- Dados de uma planilha Google Sheets

Usa um backend Flask para proteger as chaves de API.

## ✨ Como publicar no Render

1. Cria conta em https://render.com
2. Faz deploy do backend (este repositório) como "Web Service":
   - Start Command: `python app.py`
   - Variáveis de ambiente:
     - `WEATHER_API_KEY`
     - `SHEETS_API_KEY`
3. Cria um Static Site com o ficheiro `index.html`
   - Publish directory: `.`
   - Atualiza `index.html` para usar o domínio do backend

## 🔗 Endpoints

- `/weather`: Clima atual do Porto
- `/sheet-data`: Dados da planilha