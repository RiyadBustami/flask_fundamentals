from flask import Flask, render_template,redirect, request, session
app=Flask(__name__)
app.secret_key="It's so secret nobody even knows, not even me"

@app.route("/")
def index():
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=1
    
    return render_template("index.html",counter=session['counter'])

@app.route('/destroy_session',methods=['POST'])
def destroy():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)