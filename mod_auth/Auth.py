from fastapi import APIRouter, Depends, HTTPException, Header
from mod_funcionario.Funcionario import Funcionario
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB
from fastapi import Depends
import security

# dependências de forma global
router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] )

@router.post("/auth", response_model=dict)
def authenticate_user(cpf: str = Header(...), senha: str = Header(...)):
    try:
        session = db.Session()
        funcionario = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == cpf).first()

        if funcionario and senha == funcionario.senha:
            # Senha válida, retorna os detalhes do funcionário
            if funcionario.grupo == 0:
                funcionario.grupo = 'Atendente'
            elif funcionario.grupo == 1: 
                funcionario.grupo = 'Caixa'
            elif funcionario.grupo == 2: 
                funcionario.grupo = 'Administrador'
            return {
                "id_funcionario": funcionario.id_funcionario, 
                "nome": funcionario.nome, 
                "matricula": funcionario.matricula, 
                "grupo": funcionario.grupo}
        else:
            # Senha inválida ou funcionário não encontrado
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
    except Exception as e:
        print(f"Erro na validação de login: {str(e)}")
        raise HTTPException(status_code=403, detail="Erro na validação de login")