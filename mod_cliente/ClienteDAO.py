from fastapi import APIRouter
from mod_cliente.Cliente import Cliente

router = APIRouter()

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE

#GET
@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

#POST
@router.post("/cliente/", tags=["Cliente"])
def post_cliente(c: Cliente):
    return {"msg": "post executado", "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone, "compra_fiado": c.compra_fiado, "dia_fiado": c.dia_fiado, "senha": c.senha}, 200

#PUT
@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, c:Cliente):
    return {"msg": "put executado", "nome": c.nome, "cpf": c.cpf, "telefone": c.telefone, "compra_fiado": c.compra_fiado, "dia_fiado": c.dia_fiado, "senha": c.senha}, 201

#DELETE
@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201