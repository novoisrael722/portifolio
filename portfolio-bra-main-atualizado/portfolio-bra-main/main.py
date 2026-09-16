# Importar
from flask import Flask, render_template, request


app = Flask(__name__)


# Conteúdo da página e processamento dos formulários
@app.route('/', methods=['GET', 'POST'])
def index():
    selected_project = None

    # Formulário de feedback
    email = None
    text = None

    if request.method == 'POST':
        # Habilidades Dinâmicas
        projects = {
            'button_python': 'python-project.png',
            'button_discord': 'discord.png',
            'button_html': 'html.png',
            'button_db': 'db.webp'
        }

        for button, image in projects.items():
            if request.form.get(button):
                selected_project = image
                break

        # Formulário de feedback
        email = request.form.get('email')
        text = request.form.get('text')

        if email and text:
            print('E-mail:', email)
            print('Feedback:', text)

    return render_template(
        'index.html',
        selected_project=selected_project,
        email=email,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)
