from flask_sqlalchemy import SQLAlchemy

# PARTE 1 - MODELO BASE
# Este objeto db se importa en app.py para conectar Flask con SQLite.
db = SQLAlchemy()


class Contacto(db.Model):
    # Tabla sencilla para representar contactos del directorio.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"{self.nombre} - {self.telefono}"
