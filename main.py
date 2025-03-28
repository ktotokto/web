from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    training_title, src = ("Инженерные тренажеры", "i_1.png") if "инженер" in prof or "строитель" in prof else ("Научные тренажеры", "i_2.png")
    src = url_for('static', filename=f'images/{src}')
    return render_template('training.html', training_title=training_title, src=src)

if __name__ == '__main__':
    app.run(debug=True)
