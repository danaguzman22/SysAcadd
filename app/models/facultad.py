from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db
from app.models.universidad import Universidad

class Facultad(db.Model):
    __tablename__ = 'facultades'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(db.String(100), nullable=False)
    abreviatura: Mapped[str] = mapped_column(db.String(10), nullable=False)
    directorio: Mapped[str] = mapped_column(db.String(100), nullable=False)
    sigla: Mapped[str] = mapped_column(db.String(10), nullable=False)
    codigo_postal: Mapped[str] = mapped_column(db.String(10), nullable=True)
    ciudad: Mapped[str] = mapped_column(db.String(50), nullable=True)
    domicilio: Mapped[str] = mapped_column(db.String(100), nullable=True)
    telefono: Mapped[str] = mapped_column(db.String(20), nullable=True)
    contacto: Mapped[str] = mapped_column(db.String(100), nullable=True)
    email: Mapped[str] = mapped_column(db.String(100), nullable=False)
    universidad_id: Mapped[int] = mapped_column(
        db.Integer,
        db.ForeignKey('universidades.id'),
        nullable=False
    )
    universidad: Mapped["Universidad"] = relationship('Universidad', backref='facultades')
