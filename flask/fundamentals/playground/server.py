from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route('/play/<int:x>/<string:color>')
def box(x,color):
    return render_template("index.html", id = "box", times = x, color = color)



# 
# 
# 
if __name__ == "__main__":
    app.run(debug = True)