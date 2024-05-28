from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página inicial que muestra las opciones iniciales del juego
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la lógica de la elección del usuario
@app.route('/handle_data', methods=['POST'])
def handle_data():
    choice = request.form['choice']
    if choice == 'option1':
        return redirect(url_for('out1'))
    elif choice == 'option2':
        return redirect(url_for('out2'))
    else:
        return redirect(url_for('out3'))

# Páginas de resultados
@app.route('/outcome_one')
def outcome_one():
    return render_template('out1.html')

@app.route('/outcome_two')
def outcome_two():
    return render_template('out2.html')

@app.route('/outcome_three')
def outcome_three():
    return render_template('out3.html')

if __name__ == "__main__":
    app.run(debug=True)
