from app.models import Universidad
from app.repositories import UniversidadRepository



class UniversidadService:

    @staticmethod
    def crear_Universidad(universidad: Universidad):
        UniversidadRepository.crear(universidad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Universidad:
        return UniversidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Universidad]:
        return UniversidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_Universidad(id: int, universidad: Universidad) -> Universidad:
        universidad_existente = UniversidadRepository.buscar_por_id(id)
        if not universidad_existente:
            return None
        universidad_existente.nombre = universidad.nombre
        universidad_existente.sigla = universidad.sigla
        return universidad_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Universidad:
        universidad = UniversidadRepository.buscar_por_id(id)
        if not universidad:
            return None
        return universidad
    
        