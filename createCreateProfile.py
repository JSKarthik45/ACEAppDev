from jinja2 import Template as t
import pyhtml as h

s = h.html(
    h.head(
        h.meta(charset = "UTF-8"),
        h.meta(name = "author", content = "J S Karthik"),
        h.meta(name = "description", content = "Create Profile Page"),
        h.title("Create Profile"),
        h.link(rel = "stylesheet", href = "../static/style.css")
    ),
    h.body(
        h.h3("Create Profile"), 
        h.form(method = "POST", enctype="multipart/form-data") (
            "{% for i in a %}", 
            h.div(
                h.span(style = "display: inline-block; width: 150px")("{{i}}"),
                h.input_(type = "{{a[i][1]}}", name = "{{a[i][0]}}", id = "textinput")
            ),
            "{% endfor %}",
            h.br(),
            h.div(
                h.input_(type = "submit", id = "buttoninput"),
                h.input_(type = "reset", id = "buttoninput", style = "margin-left: 250px;")
            )
        )
    )
)
d = {"Mail Id" : ["email", "email"], "Department" : ["dep", "text"], "Github Link" : ["gitlink", "url"], "Description" : ["desc", "text"], "Upload JPEG Profile Picture" : ["profpic", "file"]}
htmlcontent = t(s.render()).render(a = d)

writeToCreateProfile = open("../templates/CreateProfile.html", "w")
writeToCreateProfile.write(htmlcontent)
writeToCreateProfile.close()
