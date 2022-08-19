import email
# from inspect import _SourceObjectType
from msilib.schema import Component
from flask import Flask,render_template,url_for,request,redirect
import csv
app= Flask(__name__)
print(__name__)

@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        database.write(f'\n{email},{subject},{message}')
def write_to_csv(data):
         with open ('database.csv',mode='a',newline="") as database2:
            email=data['email']
            subject=data['subject']
            message=data['message']
            csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["Email", "Subject", "Message"])
            csv_writer.writerow([email,subject,message])
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
         
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went worng'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/favicon.ico') 
# def blog():
#     return 'These are my thoughts on blogs...'  

# @app.route('/project.html')
# def Project_page():
#     return render_template('project.html')

# @app.route('/components.html')
# def component_page():
#     return render_template('components.html')  