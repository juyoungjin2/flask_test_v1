from flask import Flask, render_template, request
import random
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./static/image') if isfile(join('./static/image', f))]

app = Flask(__name__)


@app.route("/")

def hello():
    form = random.choice(onlyfiles)
    return render_template('index.html',form=form)

form = random.randint(0,100)
@app.route("/test", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            rand_num = random.randint(1,10)
            return rand_num
            # pass  # do something
        elif request.form.get('action2') == 'VALUE2':
            rand_num = random.randint(1, 10)
            return rand_num
            # pass  # do something else
        else:
            rand_num = random.randint(1, 10)
            return rand_num
            # pass  # unknown
    elif request.method == 'GET':
        return render_template('test.html', form=form)

    return render_template("index.html")





if __name__ == '__main__':
    app.run(debug=True)