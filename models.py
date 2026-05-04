from flask_sqlalchemy import SQLAlchemy

# PARTE 3 - MODELO MINIMO PARA PROBAR LA VISTA
# Persona B puede usar este mismo modelo para renderizar datos de ejemplo.
db = SQLAlchemy()


class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
