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
        content = r.content.decode('utf-8')
        try:
            d = r.json()
            return jsonify({
                'funding_rate': float(d['result']['funding_rate']),
                'timestamp': d['time_now'],
                'raw_response': content
            })
        except Exception as e:
            return jsonify({'error': f'JSON decode error: {str(e)}', 'raw_response': content})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/open_interest')
def get_open_interest():
    url = "https://api.bybit.com/open-api/open-interest?symbol=BTCUSD"
    try:
        r = requests.get(url)
        content = r.content.decode('utf-8')
