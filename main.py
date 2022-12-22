import store 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app =FastAPI()

@app.get('/')
def get_list():
    return[
        1,2,3,4
    ]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
    <h1>Hola, bienvenido a mi primera pagina</h1>
    <p>Mi nombre es lucia, espero que esto no muera aca nada mas</p>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()