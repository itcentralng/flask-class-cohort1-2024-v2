from flask import Flask, request, render_template

app = Flask(__name__)

# GET - retrieve data form server
# POST - Send data to the server
# PUT - Update data on the server
# PATCH - Partially update data on the server
# DELETE - Delete data from the server

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('index.html', name="Kundil", person="Muhammad")
    return render_template('index.html')

@app.get('/home')
def get_home():
    return render_template('home.html')

@app.post('/home')
def post_home():
    return render_template('home.html', age=16, weight=19.2)