from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('index.html', name="Shehu", person="Muhammad")
    return render_template('index.html')

@app.get('/home')
def get_home():
    return render_template('home.html')

@app.post('/home')
def post_home():
    return render_template('home.html', age=20, weight=30)