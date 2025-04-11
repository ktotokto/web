import secrets
from flask import Flask, render_template, redirect
from pygame.examples.cursors import color_cursor

from forms import emergency_access

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<string:prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<string:list_input>')
def list_prof(list_input):
    list_pr = ["инженер-иследователь", "пилот", "строитель", "экзобиолог", "врач",
               "инженер по терраформированию", "климатолог",
               "специалист по радиационной защите", "астрогеолог", "гляциолог",
               "инженер жизнеобеспечения", "метеоролог", "оператор марсохода",
               "киберинженер", "штурман", "пилот дронов"]
    return render_template('list_prof.html',
                           list=list_input, list_prof=list_pr)


@app.route('/auto_answer')
@app.route('/answer')
def auto_answer():
    answer_dict = {"title": "Анкета", "surname": "Watny", "name": "Mark",
                   "education": "выше среднего", "profession": "штурман марсохода", "sex": "male",
                   "motivation": "Всегда мечтал застрять на Марсе!", "ready": True}
    return render_template('auto_answer.html', dict=answer_dict, title=answer_dict["title"])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = emergency_access.LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/distribution')
def distribution():
    list_astronauts = ["Ридли Скотт", "Эндри Уир", "Марк Уотни"]
    return render_template('distribution.html', list_astronauts=list_astronauts)


@app.route('/table/<string:sex>/<string:age>')
def table(sex, age):
    age = int(age)
    if age < 255:
        color = (0 + age, 0 + age, 255 - age) if sex == 'male' else (255 - age, 0 + age, 0 + age)
    else:
        color = (0, 0, 0)
    image = "age_%21.png" if age < 21 else "age_21%.png"
    return render_template('table.html', image=f"images/{image}", color=color)


if __name__ == '__main__':
    app.run(debug=True)
