from flask import Flask, render_template,request,redirect,url_for
import csv

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
checkheader=0

@app.route("/submit_form",methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        form = request.form.to_dict()
        write_to_csv(form)
        return render_template("submit.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    global checkheader
    with open('database.csv', 'a',newline='') as csvfile:
        writer=csv.DictWriter(csvfile, fieldnames = list(data.keys()))
        if checkheader==0:
            writer.writeheader()
            checkheader=1
        writer.writerow(data)
        print("CSV Modified")

