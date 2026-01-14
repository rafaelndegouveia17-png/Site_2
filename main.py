from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Mel nunca estraga.",
    "Bananas são frutas, mas morangos não são.",
    "Um grupo de flamingos é chamado de 'flamboyance'.",
    "Polvos têm três corações.",
    "A cocô de wombat tem forma de cubo.",
    "Mel nunca estraga e pode ser consumido mesmo após milhares de anos.",
    "As abelhas visitam cerca de 50 a 100 flores durante uma colheita de néctar.",
    "Um caracol pode dormir por até 3 anos.",
    "Os ursos polares têm pele preta sob seu pelo branco.",
    "As vacas têm melhores amigas e ficam tristes quando separadas.",
    "Os gatos têm um terceiro pálpebra chamada 'nictitante'.",
    "Alguns peixes podem subir em árvores.",
    "As tartarugas podem viver mais de 150 anos.",
    "Os golfinhos têm nomes únicos e se chamam pelo nome."
]

@app.route('/')
def home():
    return '<h1>Página inicial</h1>' \
        '<p>Bem-vindo ao site!</p>' \
        '<p><a href="/facts">Veja um fato aleatório!</a></p>'\
        '<p><a href="/cara e coroa">Jogue Cara ou Coroa!</a></p>'\
        '<p><a href="/gerador de senhas">Gerador de Senhas</a></p>'     
        


@app.route('/facts')
def facts_route():
    random_fact = random.choice(facts_list)
    return f'<p>{random_fact}</p>'
@app.route('/cara e coroa')
def cara_coroa():
    return f'<p>Resultado: {"Cara" if random.choice([True, False]) else "Coroa"}</p>'
@app.route('/gerador de senhas')
def gerador_senhas():
    numero = random.randint(1, 9999)
    return '<h1>Gerador de senhas</h1>' \
           f'<p>{numero}</p>'

           
app.run(debug=True)
