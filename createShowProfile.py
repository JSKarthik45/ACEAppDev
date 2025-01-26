import pyhtml as h

s = h.html(
    h.head(
        h.meta(charset = "UTF-8"),
        h.meta(name = "author", content = "J S Karthik"),
        h.meta(name = "description", content = "Show Profile Page"),
        h.title("Create Profile"),
        h.link(rel = "stylesheet", href = "../static/style.css")
    ),
    h.body(
        h.img(src = "../static/uploads/{{ username }}.jpeg", alt = "Profile Picture", width = "150px" , height = "150px", style = "vertical-align: top; display: inline-block; margin-top: 30px"),
        h.div(style = "display: inline-block; margin-left: 50px;") (
        h.div (
            h.h4(
                "Username: "
            ),
            h.span(
                "{{ username }}"
            )
        ),
        h.div (
            h.h4(
                "Mail Id: "
            ),
            h.span(
                "{{ email }}"
            )
        ),
        h.div (
            h.h4(
                "Department: "
            ),
            h.span(
                "{{ dep }}"
            )
        )),
        h.br(),
        h.div(style = "display: inline-block;") (
        h.div(
            h.br(), h.br(), 
            h.span(style = "margin-left: 30px;")(
                h.a(href = "{{ gitlink }}", target = "_blank") (
                    "Github Link"
                )
            )
        ),
        h.div(
            h.h4(style = "margin-left: 30px;")(
                "Description: "
            ),
            h.span(style = "margin-right: 60px;")(
                "{{ desc }}"
            )
        )),
        h.form(method = "POST", style = "vertical-align: top; margin-top: 50px;") (
            h.input_(type = "submit", name = "home", value = "Home", id = "buttoninput", title = "Go To Home")
        )
    )
)

s = s.render()
