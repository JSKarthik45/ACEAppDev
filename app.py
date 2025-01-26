from flask import Flask as f, render_template as rt, request as r, redirect as re, url_for as url, flash
from jinja2 import Template as t
from HTMLGeneration.createShowProfile import s
from HTMLGeneration.createHomePage import c
import os

'''Create a simple Web Application which takes the following user input: 
Username, Mail ID, Department, Project Links and Description and an option to upload profile image.

It must display the user profile information as personal profile page filled with the 
information given by any user.'''

app = f(__name__)
app.secret_key = "abcd"

currentUserWrite = open("data/CurrentUser.csv", "w")
currentUserWrite.write("img")
currentUserWrite.close()

@app.route("/", methods = ["GET", "POST"])
def home() :
    if(r.method == "GET") :
        currentUserRead = open("data/CurrentUser.csv", "r")
        u = currentUserRead.read()
        currentUserRead.close()
        htmlcontent = t(c).render(username = u)
        HomePageWrite = open("templates/index.html", "w")
        HomePageWrite.write(htmlcontent)
        HomePageWrite.close()
        return rt("index.html")
    elif(r.method == "POST") :
        if("signin" in r.form) :
            return re(url("signIn"))
        elif("viewprofile" in r.form) :
            currentUserRead = open("data/CurrentUser.csv", "r")
            u = currentUserRead.read()
            currentUserRead.close()
            
            if(u != "img") :
                return re(url("showProfile", username = u))
            else :
                return re(url("signIn"))

@app.route("/signIn", methods=["GET", "POST"])
def signIn():
    if r.method == "GET":
        return rt("signIn.html")
    elif r.method == "POST":
        username = r.form.get("username")
        password = r.form.get("password")
        if("signin" in r.form):
            currentUserWrite = open("data/CurrentUser.csv", "w")
            currentUserWrite.write(username)
            currentUserWrite.close()
            return verify(username, password)
        elif("signup" in r.form):
            signupwrite = open("data/UsernamePassword.csv", "a")
            res = checkUsernamePassword(username, password)
            currentUserWrite = open("data/CurrentUser.csv", "w")
            currentUserWrite.write(username)
            currentUserWrite.close()
            if(res):
                return res
            signupwrite.write(f"{username}, {password}\n")
            signupwrite.close()
            return re(url("createProfile", username = username, password = password))
        
def verify(u, p):
    if len(u) == 0:
        flash("Invalid Username")
        return re(url("signIn"))
    elif len(p) == 0:
        flash("Invalid Password")
        return re(url("signIn"))
    with open("data/UsernamePassword.csv", "r") as signupread:
        for i in signupread.readlines():
            j = i.split(", ")
            if(j[0] == u):
                if(j[1].strip() == p):
                    return re(url("showProfile", username = u))
    flash("Invalid Username or Password")
    return re(url("signIn"))

def checkUsernamePassword(u, p):
    if(len(u) == 0):
        flash("Invalid Username")
        return re(url("signIn"))
    elif(len(p) == 0):
        flash("Invalid Password")
        return re(url("signIn"))
    with open("data/UsernamePassword.csv", "r") as signupread:
        for i in signupread.readlines():
            j = i.split(", ")
            if(u == j[0]):
                flash(f"{u} Is Not Available")
                return re(url("signIn"))
    return None

@app.route("/createProfile", methods = ["GET", "POST"])
def createProfile() :
    if(r.method == "GET") :
        return rt("createProfile.html")
    elif(r.method == "POST") :
        username = r.args.get("username")
        password = r.args.get("password")
        email = r.form.get("email")
        dep = r.form.get("dep")
        gitlink = r.form.get("gitlink")
        desc = r.form.get("desc")
        profpic = r.files.get("profpic")
        if profpic:
            profpic.save(f"static/uploads/{username}.jpeg")
        profdata = open("data/ProfileData.csv", "a")
        profdata.write(f"{username}, {password}, {email}, {dep}, {gitlink}, {desc}\n")
        profdata.close()
        return re(url("showProfile", username = username))

@app.route("/showProfile", methods = ["GET", "POST"])
def showProfile() :
    if(r.method == "GET") :
        username = r.args.get("username")
        profile_image_filename = f"{username}.jpeg"
        profdata = open("data/ProfileData.csv", "r")
        for i in profdata.readlines():
            if i.split(",")[0].strip() == username :
                data = [x.strip() for x in i.split(",")]
        profdata.close()
        htmlcontent = t(s).render(username = data[0], email = data[2], dep = data[3], gitlink = data[4], desc = data[5])
        showProfileWrite = open("templates/showProfile.html", "w")
        showProfileWrite.write(htmlcontent)
        showProfileWrite.close()
        return rt("showProfile.html", prof = profile_image_filename)
    elif(r.method == "POST") :
        return re(url("home"))

if __name__ == "__main__" :
    app.debug = True
    app.run(debug = True)