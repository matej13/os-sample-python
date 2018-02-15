from flask import Flask
application = Flask(__name__)

@application.route("/")
#def hello():
#    return "Hello World!123"
def test(x): #program does nothing as written
    return "Test to see if it works" 
    x = 5
    return "test234" + x

if __name__ == "__main__":
    application.run()
