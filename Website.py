from flask import Flask, render_template, request, redirect, url_for
import gpadata


app = Flask(__name__)

"""
mainpage
inputs-none
returns-template for home page
"""


@app.route('/')
def mainpage():
    return render_template("website code.html")


"""
data
input-none
this is the function that runs when you hit the search button. It takes the input text and goes to the data page
returns-data page
"""


@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == "POST":
        abrv = request.form['abrvbox']
        global text
        text = abrv
        return redirect(url_for('datascreen', name=abrv))
    else:
        abrv = request.form['abrvbox']
        return redirect(url_for('datascreen', name=abrv))


"""
datascreen
input-none
this is the function that makes the datatable on the webpage
returns data page with webpage
"""


@app.route('/datascreen/<name>')
def datascreen(name):
    x = gpadata.make_dataframe(name)
    if (type(x) == str):
        return "error not a valid subject"
    return render_template("makedata.html", data=x.to_html())


"""
goback
input-none
this function is called whenever the buttons on the data page are pressed. Depending on the button 
it either sorts the data, reccomends a class time or goes back to the home page
"""


@app.route('/datascreen', methods=["GET", "POST"])
def goback():
    if request.method == "POST":
        if request.form['submit button'] == 'reset':
            return render_template("website code.html")
        elif request.form['submit button'] == 'sort':
            x = gpadata.make_sorted_dataframe(text)
            return render_template("makedata.html", data=x.to_html())
        elif request.form['submit button'] == 'reverse_sort':
            x = gpadata.make_reverse_sorted_dataframe(text)
            return render_template("makedata.html", data=x.to_html())
        elif request.form['submit button'] == 'reccomend':
            x = gpadata.make_sorted_dataframe(text)
            return render_template("makedata.html", data = x.to_html())

        else:
            return "error"


if __name__ == '__main__':
    app.run()
