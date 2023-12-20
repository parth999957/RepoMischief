# from flask import Flask, render_template, request

# # app = Flask(__name__)

# # @app.route('/', methods = ["POST", "GET"])  
# # def login():
# #     ocoords = request.form(['obstacles'])
# #     rows = request.form(['rows'])
# #     cols = request.form(['columns'])
# #     start = request.form(['start'])
# #     goal = request.form(['goal'])
# #     return render_template("index.html")   



from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/BFS/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['obstacles']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('obstacles')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)

