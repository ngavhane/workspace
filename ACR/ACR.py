from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from classify_crash import ClassifyCrash

app = Flask(__name__)
#app.config['MONGO_DBNAME'] = 'restdb'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    connection = MongoClient("ds117913.mlab.com",17913)
    handle = connection["acr"]
    handle.authenticate("niteengavhane4p","Boysarebest@1")
    return handle

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/delete_form')
def delete_form():
    return render_template('form_delete.html')


@app.route('/form_submit_crash')
def crash_submit_page():
    return render_template('form_submit_crash.html')

@app.route('/submit_crash_report/', methods=['POST'])
def submit_crash_report():
    crash_content = request.form['crash_content']
    print crash_content
    handle.mycollection.insert_one({"crash_content": crash_content})
    return render_template('show_crash_content.html', crash_content=crash_content)


@app.route('/classify_crash_report/', methods=['POST'])
def classify_crash_report():
    for info in handle.mycollection.find():
        print "I am in classify crash report tool"
        crash_type = info["crash_type"]
        crash_content = info["crash_content"]
        print "*****"
        ClassifyCrash().crash_classify(crash_type, crash_content, crash_re="^r()")
        
    return render_template('classify_result.html')
@app.route('/form')
def form():
    return render_template('form_submit.html')

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    print name
    print email
    handle.mycollection.insert_one({"name": name, "email": email})
    return render_template('form_action.html', name=name, email=email)

@app.route('/show_form', methods=['GET'])
def show_form():
    for info in handle.mycollection.find():
            name=info["name"]
            email= info["email"]
    
    return render_template('form_action.html', name=name, email=email)

@app.route('/delete_all', methods=['POST'])
def delete_all():
    handle.mycollection.drop()
    return render_template('form_action.html', crash_content = "deleted all")

@app.route('/list_all_crashes', methods=['GET'])
def list_all_crashes():
    for info in handle.mycollection.find():
        print info
        crash_content = info["crash_content"]
    
    return render_template('form_action.html', crash_content=crash_content)
        


if __name__ == '__main__':
    handle = connect()
    app.run()
