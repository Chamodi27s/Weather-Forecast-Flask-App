from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# 🔑 Replace this with your free key from https://www.weatherapi.com/
API_KEY = "ab35e20255d4411cbdd154426250510"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {'key': API_KEY, 'q': city}
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            # Check if API returned valid data
            if 'error' not in data:
                weather = {
                    'city': data['location']['name'],
                    'country': data['location']['country'],
                    'temperature': data['current']['temp_c'],
                    'condition': data['current']['condition']['text'],
                    'icon': data['current']['condition']['icon'],
                    'humidity': data['current']['humidity'],
                    'wind': data['current']['wind_kph']
                }
            else:
                weather = {'error': 'City not found!'}
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
