c = '''
<!DOCTYPE html> 
<html>
    <head>
        <meta charset = "UTF-8"/>
        <meta name = "author" content = "J S Karthik"/>
        <meta name = "description" content = "Home Page"/>
        <title>
            Home
        </title>
        <link rel = "stylesheet" href = "../static/style.css">
    </head>
    <body>
        <h1>
            ACE Recruitments '25 - Web Development
        </h1>
        <form method = "POST" style = "margin-left: 390px;">
            <input type = "submit" name = "signin" value = "Sign In" id = "buttoninput" title = "Sign In">
            <input type = "submit" name = "viewprofile" value = "Profile" id = "buttoninput" title = "View Profile">
            <img src = "../static/uploads/{{ username }}.jpeg" width = 50 height = 50 alt = "profile picture">
        </form>
    </body>
</html>
'''