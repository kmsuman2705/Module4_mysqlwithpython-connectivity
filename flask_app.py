from flask import Flask

app = Flask(__name__)

# Route 1: Home Page
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Route 2: About Page
@app.route('/about')
def about():
    return "This is the About Page."

# Route 3: Contact Page
@app.route('/contact')
def contact():
    return "Contact us at contact@example.com."

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
