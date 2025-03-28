from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
