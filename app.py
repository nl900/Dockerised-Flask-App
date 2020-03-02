from flask import Flask, render_template
 
app = Flask(__name__)
 
 
@app.route('/')
def hello_flask():
    #return "Hello world"
    return render_template("whale_gif.html")
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
