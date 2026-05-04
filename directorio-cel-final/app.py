from flask import Flask, render_template, request, redirect, url_for
from models import db, Contacto


# PARTE 4 - VERSION FINAL INTEGRADA
# Merge conceptual de:
# - Parte 1: base Flask + SQLite + modelo Contacto.
# - Parte 2: rutas /add y /search.
# - Parte 3: vista HTML con formularios y tabla.

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contactos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def crear_datos_iniciales():
    # Evita iniciar el directorio vacio en la primera ejecucion.
    if Contacto.query.count() == 0:
        db.session.add(Contacto(nombre="Ana Perez", telefono="3001112233"))
        db.session.add(Contacto(nombre="Luis Gomez", telefono="3104445566"))
        db.session.commit()


@app.route("/")
def index():
    # Controlador: consulta el modelo y envia los datos a la vista.
    contactos = Contacto.query.all()
    return render_template("index.html", contactos=contactos, busqueda="")


@app.route("/add", methods=["POST"])
def add():
    # Los nombres "nombre" y "telefono" coinciden con los inputs del HTML.
    nombre = request.form.get("nombre")
    telefono = request.form.get("telefono")

    nuevo_contacto = Contacto(nombre=nombre, telefono=telefono)
    db.session.add(nuevo_contacto)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/search")
def search():
    # El input de busqueda se llama "q" en el HTML.
    q = request.args.get("q", "")
    contactos = Contacto.query.filter(Contacto.nombre.contains(q)).all()

    return render_template("index.html", contactos=contactos, busqueda=q)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        crear_datos_iniciales()

    app.run(debug=True)
