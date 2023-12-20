from flask import Flask, render_template, request
from main import Navigate
from map import MAP

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    obstacles = request.form['obstacles']
    nrow = request.form['rows']
    ncol = request.form['columns']
    start = request.form['start']
    goal = request.form['goal']

    print("Obstacles:", obstacles)
    print("Rows:", nrow)
    print("Columns:", ncol)
    print("Start:", start)
    print("Goal:", goal)

    maps = MAP(nrow, ncol, start, goal, obstacles)
    navigation = Navigate(maps)
    navigation.search_astar()


    # Return some response or render a template
    return "Form submitted! Check console for output."

if __name__ == '__main__':
    app.run(debug=True)
