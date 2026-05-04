from flask import Flask, request, redirect, url_for
from models import db, Contacto


# PARTE 2 - BACKEND EN BRANCH / SERVICIOS EXTRA
# Esta version extiende el controlador con:
# - Ruta /add para registrar contactos.
# - Ruta /search para buscar contactos por nombre.

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contactos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def crear_datos_iniciales():
    if Contacto.query.count() == 0:
        db.session.add(Contacto(nombre="Ana Perez", telefono="3001112233"))
        db.session.add(Contacto(nombre="Luis Gomez", telefono="3104445566"))
        db.session.commit()


@app.route("/")
def index():
    contactos = Contacto.query.all()
    texto = "Directorio de Contactos\n\n"

    for contacto in contactos:
        texto += f"{contacto.nombre} - {contacto.telefono}\n"

    return f"<pre>{texto}</pre>"


@app.route("/add", methods=["POST"])
def add():
    # Flujo simple: controlador recibe datos del formulario y los guarda en el modelo.
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")

    nuevo_contacto = Contacto(nombre=nombre, telefono=telefono)
    db.session.add(nuevo_contacto)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/search")
def search():
    # Busca contactos cuyo nombre contenga el texto enviado en el parametro q.
    q = request.args.get("q")
    contactos = Contacto.query.filter(Contacto.nombre.contains(q)).all()

    texto = f"Resultados de busqueda para: {q}\n\n"
    for contacto in contactos:
        texto += f"{contacto.nombre} - {contacto.telefono}\n"

    return f"<pre>{texto}</pre>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        crear_datos_iniciales()

    app.run(debug=True)
