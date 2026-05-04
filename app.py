from flask import Flask, render_template
from models import db, Contacto


# PARTE 3 - FRONTEND EN BRANCH / INTERFAZ
# Esta version se concentra en mostrar la vista HTML.
# Las rutas /add y /search se conectaran al integrar con el backend final.

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
    return render_template("index.html", contactos=contactos)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        crear_datos_iniciales()

    app.run(debug=True)
