from flask import Flask, render_template

app = Flask(__name__)

c=[0]

@app.route('/')
def index():
    
    return render_template('index.html', count=c)

@app.route('/increment')
def increment_count():
    c[0] += 1
    return render_template('count_display.html', count=c)

@app.route('/decrement')
def decrement_count():
    c[0] -= 1
    return render_template('count_display.html', count=c)



if __name__ == '__main__':
    app.run(debug=True)