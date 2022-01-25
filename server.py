import csv
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/<string:page>")
def html_page(page):
    return render_template(page)


def write_db(data):
    with open('database.txt',mode='a') as db:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=db.write(f'\n{email},{subject},{message}')

def write_csv(data):
    with open('database.csv',mode='a',newline='\n') as db:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(db, delimiter=',')
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_db(data)
            write_csv(data)
            return redirect('thanks.html')
        except:
            return 'Unable to save your data, Try Again'
    else:
        return 'Oops!! Something went Wrong'
