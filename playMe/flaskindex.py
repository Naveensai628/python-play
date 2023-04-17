from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    title='PlayMe'
    name = 'Naveen Sai'
    return render_template('index.html', name = name, title=title)

app.run(debug=True)