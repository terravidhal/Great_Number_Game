from flask import Flask, render_template, redirect, request, session  # added session!
import random    # import the random module


app = Flask(__name__)
app.secret_key = '' # python -c 'import secrets; print(secrets.token_hex())'

@app.route("/") 
def home():
    if 'rand_numb' not in session:  
      session["rand_numb"] = random.randint(1, 100)  # random number between 1-100

    if "mssg_reslt" not in session:    
        session["mssg_reslt"] = '' 

    if "usr_numb" not in session:    
        session["usr_numb"] = 0 

    if "add_count" not in session:    
        session["add_count"] = 0 

    if "array_infos" not in session:    
        session["array_infos"] = ''

    return render_template("index.html", rand_number = session["rand_numb"], mssg_result = session["mssg_reslt"],user_number = session["usr_numb"])


# @app.route("/destroy_session", methods=["POST"])
# def destroy_sess():
#     session.clear()
#     return redirect("/")

# 

@app.route("/destroy_session", methods=["POST"])
def destroy_sess():
    session.pop('rand_numb')
    session.pop('mssg_reslt')
    session.pop('usr_numb')
    session.pop('add_count')
    return redirect("/")


@app.route("/random_numb", methods=["POST"])
def specify_increment():
    session["usr_numb"] =  int(request.form["random_number"])

    if session["usr_numb"]  > session["rand_numb"] :
      session["mssg_reslt"] = "Too_high"
    elif session["usr_numb"]  < session["rand_numb"] :
      session["mssg_reslt"] = "Too_low"
    elif session["usr_numb"]  == session["rand_numb"]:
       session["mssg_reslt"] = "success"
    # BONUS NINJA
    session["add_count"] += 1
    return redirect("/")

# BONUS SENSEI
@app.route("/shows_winners", methods=["POST"])
def shows_win():
    print(session["array_infos"])
    session['array_infos'] += f"<div class='green'>Winner: {request.form['name_winners']} and counts_attempts: {request.form['counts_attempts']}</div>" 
    return render_template("show.html")



@app.errorhandler(404)  # we specify in parameter here the type of error, here it is 404
def page_not_found(
    error,
):  # (error) is important because it recovers the instance of the error that was thrown
    return f"<h2 style='text-align:center;padding-top:40px'>Sorry! No response. Try again</h2>"


if __name__ == "__main__":
    app.run(debug=True)
