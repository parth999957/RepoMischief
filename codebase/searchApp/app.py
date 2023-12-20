from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    obstacles = request.form['obstacles']
    rows = request.form['rows']
    columns = request.form['columns']
    start = request.form['start']
    goal = request.form['goal']

    print("Obstacles:", obstacles)
    print("Rows:", rows)
    print("Columns:", columns)
    print("Start:", start)
    print("Goal:", goal)



    # Return some response or render a template
    return "Form submitted! Check console for output."

if __name__ == '__main__':
    app.run(debug=True)
