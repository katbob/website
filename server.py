from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('/index.html')


@app.route('/<string:pagename>')
def render_page(pagename):
    return render_template((pagename + '.html'))


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'Email is: {email} \n'
                              f'Subject is: {subject} \n'
                              f'Message is: {message}\n\n')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return "didn't save to database"
    else:
        return 'something went wrong'
