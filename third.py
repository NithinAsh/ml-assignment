from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates')

with open('model_nithin.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            result = "The Species is Iris-Setosa"
        elif prediction[0] == 1:
            result = "The Species is Iris-Versicolor"
        else:
            result = "The Species is Iris-Virginica"

        return render_template('second.html', result=result)

    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True)
