from flask import Flask
from models import db, Contacto


# PARTE 1 - BACKEND BASE / MAIN
# En esta version se crea el nucleo del proyecto:
# Flask + SQLite + modelo Contacto + consulta basica.

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contactos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


def crear_datos_iniciales():
    # Inserta datos de muestra solo si la tabla esta vacia.
    if Contacto.query.count() == 0:
        contacto1 = Contacto(nombre="Ana Perez", telefono="3001112233")
        contacto2 = Contacto(nombre="Luis Gomez", telefono="3104445566")

        db.session.add(contacto1)
        db.session.add(contacto2)
        db.session.commit()


@app.route("/")
def index():
    # Ruta principal: consulta todos los contactos.
    contactos = Contacto.query.all()
    texto = "Directorio de Contactos\n\n"

    for contacto in contactos:
        texto += f"{contacto.nombre} - {contacto.telefono}\n"

    return f"<pre>{texto}</pre>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        crear_datos_iniciales()

        # LOGICA TEMPORAL DE CONSOLA
        # Este bloque se puede eliminar cuando exista una vista HTML funcional.
        respuesta = input("Desea ver el directorio? (s/n): ")

        if respuesta.lower() == "s":
            contactos = Contacto.query.all()
            print("\nDirectorio de Contactos:")
            for contacto in contactos:
                print(f"{contacto.nombre} - {contacto.telefono}")
        else:
            print("Programa finalizado.")

    app.run(debug=True)
