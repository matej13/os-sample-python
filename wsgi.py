from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"
def Test1(): #program does nothing as written
    return("Test to see if it works")

if __name__ == "__main__":
    application.run()
