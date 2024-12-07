from flask import Flask, session, render_template, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

@app.route('/')
def index():
    if 'visit_counter' in session:
        session['visit_counter'] += 1
    else:
        session['visit_counter'] = 1
        
    if 'click_counter' not in session:
        session['click_counter'] = 0
        
    return render_template('counter.html', 
                        visit_count=session['visit_counter'],
                        click_count=session['click_counter'])

@app.route('/increment', methods=['POST'])
def increment():
    if 'click_counter' in session:
        session['click_counter'] += 1
    else:
        session['click_counter'] = 1
    return jsonify({'click_count': session['click_counter']})

@app.route('/destroy_session')
def destroy_session():
    session.clear()  
    return redirect(url_for('index'))  

if __name__ == '__main__':
    app.run(debug=True)
