from flask import Flask

'''
This will create an instance of flask which will be WSGI.
'''
### WSGI Application
app=Flask(__name__)

@app.route("/") ### Decorator in rule: string format
def welcome():
    return "Welcome to Flask. I'm Mayank Tiwari. How are You?. I'm fine!"

if __name__ == '__main__':
    app.run(debug=True) ### Run the application in debug mode so any changes made will be visible directly without restarting the server.
    