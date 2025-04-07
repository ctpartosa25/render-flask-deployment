from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return render_template("contact.html", name=name, message=message, submitted=True)
    return render_template("contact.html", submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
