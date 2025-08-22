from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Simple About Me generator without OpenAI
def generate_about_me(keywords):
    if keywords.strip() == "":
        return "This is my About Me section. I am a passionate learner and professional."
    return f"This is my About Me section. I am {keywords}."

@app.route('/')
def home():
    return render_template('your_form.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    linkedin = request.form['linkedin']
    instagram = request.form['instagram']
    leetcode = request.form['leetcode']
    about_keywords = request.form['about']

    # Generate About Me without AI
    about_text = generate_about_me(about_keywords)

    # Save uploaded profile picture
    profile_pic = request.files['profile_pic']
    pic_filename = profile_pic.filename

    # Ensure uploads folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    profile_pic.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_filename))

    return render_template(
        'success.html',
        name=name,
        email=email,
        linkedin=linkedin,
        instagram=instagram,
        leetcode=leetcode,
        about=about_text,
        pic=pic_filename
    )

if __name__ == '__main__':
    app.run(debug=True)


