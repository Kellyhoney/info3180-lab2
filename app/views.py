from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime



def format_date_joined(date):
    return date.strftime('%b, %Y')


###
# Routing for your application.
### 



@app.route('/profile')
def profile():
    """Render the profile page."""
    join_date = datetime.strptime("2023-09-01", "%Y-%m-%d")  # Convert string to datetime object
    user_info = {
        "name": "Shantay Kellyman",
        "username": "@shantayk",
        "location": "Kingston, Jamaica", 
        "join_date": format_date_joined(join_date),
        "bio": "I am a creative individual passionate about marketing and web development. I enjoy learning new skills, dancing, and going to the movies.",
        "posts": 25,
        "followers": 120,
        "following": 80,
        "profile_pic": url_for('static', filename='images/profile.jpeg')  
    }
    return render_template("profile.html", user=user_info)




@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Shantay Kellyman")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
