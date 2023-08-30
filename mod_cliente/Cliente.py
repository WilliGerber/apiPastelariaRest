from pydantic import BaseModel

class Cliente(BaseModel):
    id_produto: int = None
    nome: str
    cpf: str
    telefone: str
    compra_fiado: float
    dia_fiado: str
    senha: str