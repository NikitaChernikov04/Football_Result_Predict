from flask import Flask, render_template, request, redirect, url_for
from result import calculate_probability


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['POST'])
def index():
    if request.method == 'POST':
        Home_team = request.form['Home_team']
        Enemy_team = request.form['Enemy_team']


        with open('data.txt', 'w') as f:
            f.write(f"{Home_team},{Enemy_team}")

        return redirect(url_for('result'))
    else:
        return render_template('home.html')


@app.route('/result')
def result():
    with open("data.txt", 'r') as f:
        data = f.read()
    data = data.split(sep=',')
    Home_team = data[0]
    Enemy_team = data[1]

    win_probability, loss_probability, draw_probability, home_team_expected_score, guest_team_expected_score = calculate_probability(Home_team, Enemy_team)

    return render_template('result.html', Home_team=Home_team, Enemy_team=Enemy_team, win_probability=str(win_probability)[0:4:], loss_probability=str(loss_probability)[0:4:], draw_probability=str(draw_probability)[0:4:], home_team_expected_score=str(home_team_expected_score)[0:4:], guest_team_expected_score=str(guest_team_expected_score)[0:4:])


if __name__ == "__main__":
    app.run(debug=True)
