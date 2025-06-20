from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV
data = pd.read_csv('data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('car_name', '').lower()

    result = data[
        data['Make'].astype(str).str.lower().str.contains(query) |
        data['Model'].astype(str).str.lower().str.contains(query)
    ]

    if not result.empty:
        return render_template('result.html', tables=result.to_html(classes='data', index=False), titles=result.columns.values)
    else:
        return render_template('result.html', message="Car not found!")

if __name__ == '__main__':
    app.run(debug=True)
