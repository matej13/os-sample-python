from flask import Flask
application = Flask(__name__)

@application.route("/")
#def hello():
#    return "Hello World!123"
def test(x): #program does nothing as written
    x = 5
    print x 

if __name__ == "__main__":
    application.run()
