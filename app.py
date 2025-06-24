from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'Middleware actif'})

@app.route('/funding')
def get_funding():
    url = "https://api.bybit.com/v2/public/funding/prev-funding-rate?symbol=BTCUSD"
    try:
        r = requests.get(url)
        d = r.json()
        return jsonify({
            'funding_rate': float(d['result']['funding_rate']),
            'timestamp': d['time_now']
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/open_interest')
def get_open_interest():
    url = "https://api.bybit.com/open-api/open-interest?symbol=BTCUSD"
    try:
        r = requests.get(url)
        d = r.json()
        return jsonify({
            'open_interest': float(d['result']['open_interest']),
            'timestamp': d['time_now']
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()


Add app.py
