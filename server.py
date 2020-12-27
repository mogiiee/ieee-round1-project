from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def reciever():
    return render_template('login.html')
db = {
    'user1' : 'pass1',
    'user2' : 'pass2',
    'user3' : 'pass3',
    
}


@app.route('/form_login',methods = ['POST','GET'])
def login():
    name= request.form['username']
    pwd = request.form['passwd']
    if name not in db:
        return render_template('login.html', info = "name is not right, who are you bro?")
    else:
        if db[name]!= pwd:
            return render_template('login.html', info = "password is not right, don't hack bro ")
        else:
            return render_template('inside-thing.html', name1 = name)


if __name__ == "__main__":
    app.run(debug= True)