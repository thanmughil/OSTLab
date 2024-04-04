from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_cgpa(grades, credits):
    total_credits = sum(credits)
    weighted_sum = sum(grade * credit for grade, credit in zip(grades, credits))
    cgpa = weighted_sum / total_credits
    return round(cgpa,2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    grades = []
    credits = []
    for i in range(1, 7):
        grade = float(request.form[f'grade{i}'])
        credit = float(request.form[f'credit{i}'])
        grades.append(grade)
        credits.append(credit)
    cgpa = calculate_cgpa(grades, credits)
    return render_template('result.html', cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)