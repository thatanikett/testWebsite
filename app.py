from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/health')
def health():
    # A simple 200 OK health check for AWS
    return {"status": "Healthy", "version": "v1.0.0"}, 200
    

@app.route('/simulate-error')
def error(): return "500 Internal Server Error", 500

if __name__ == '__main__':
    # Running on port 5100 locally for dev, but Docker will expose 80 to gunicorn
    app.run(host='0.0.0.0', port=5100, debug=True)