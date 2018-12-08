from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

def authentication(first,last):
    if first == "Pavan" and last == "Tirumalasetti":
        result = 'Correct'
    else:
        result = "Wrong"   
    return result

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    decision = authentication(first_name,last_name)
    if decision == "Correct":
        return 'Hello %s %s have fun learning python <br/> <a href="/">Back Home</a>' % (first_name, last_name)
    else:
        return 'Sorry! Wrong details <br/> <a href="/">Back Home</a>'

if __name__ == '__main__':
    app.run(port=3000)