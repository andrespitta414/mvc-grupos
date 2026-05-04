from flask_sqlalchemy import SQLAlchemy

# PARTE 2 - MODELO REUTILIZADO
# Se conserva el mismo modelo de la version base.
db = SQLAlchemy()


class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"{self.nombre} - {self.telefono}"
