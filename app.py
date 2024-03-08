from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render an HTML template for the homepage
    return render_template('index.html')

@app.route('/message')
def message():
    # This route will be triggered when the button is clicked
    return 'You clicked the button!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')