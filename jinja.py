from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Hello I'm Mayank Tiwari.</H1></html>"

@app.route("/index", methods=['GET']) 
def index():
    return render_template('index.html')

@app.route("/about") 
def about():
    return render_template('about.html')

@app.route("/submit", methods=['GET', 'POST']) 
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"<h1>Hello {name}. Welcome to Flask.</h1>"
    return render_template('form.html')

@app.route('/success/<score>')
def success(score):
    return 'Your score is: ' + str(score)


if __name__ == '__main__':
    app.run(debug=True)



    