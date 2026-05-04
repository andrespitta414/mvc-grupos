from flask_sqlalchemy import SQLAlchemy

# PARTE 4 - MODELO FINAL
# El modelo representa la tabla contactos dentro de SQLite.
db = SQLAlchemy()


class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"{self.nombre} - {self.telefono}"
