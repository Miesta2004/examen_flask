from flask import Flask, render_template, request, session, redirect, url_for
from models import db, Question
import os
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.urandom(24)
db.init_app(app)

# Coefficients de difficulté
DIFFICULTY_MULTIPLIERS = {
    0.5: 1,
    1.0: 2,
    2.0: 3
}

@app.route('/')
def start():
    session.clear()
    session.update({
        'current': 0,
        'score': 0,
        'start_time': time.time(),
        'time_remaining': None
    })
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'current' not in session:
        return redirect(url_for('start'))

    current_idx = session['current']
    question = Question.query.offset(current_idx).first()

    if not question:
        return redirect(url_for('resultat'))

    if request.method == 'POST':
        # Gestion timeout
        if 'timeout' in request.form:
            session['time_remaining'] = 0
            feedback = False
        else:
            answer = int(request.form.get('answer', 0))
            feedback = (answer == question.correct)
            session['time_remaining'] = None

        # Calcul du score avec coefficient
        if feedback:
            session['score'] += DIFFICULTY_MULTIPLIERS.get(question.difficulty, 1)

        session['current'] += 1
        session['last_feedback'] = feedback
        return redirect(url_for('feedback'))

    # Initialisation timer pour la question
    session['question_start'] = time.time()
    return render_template('quiz/questions.html',
                           question=question,
                           progress=current_idx+1,
                           total=Question.query.count())

@app.route('/feedback')
def feedback():
    if 'last_feedback' not in session:
        return redirect(url_for('quiz'))

    return render_template('quiz/feedback.html',
                           feedback=session.pop('last_feedback'),
                           score=session['score'],
                           progress=session['current'],  # Modification clé ici
                           total=Question.query.count())

@app.route('/resultat')
def resultat():
    total_time = round(time.time() - session['start_time'])
    return render_template('quiz/resultat.html',
                           score=session['score'],
                           total=Question.query.count(),
                           time=total_time)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)