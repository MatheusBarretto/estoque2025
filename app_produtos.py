from sqlalchemy import Engine, select
from sqlalchemy.orm import Session
from models import Categoria


def listar(engine: Engine):
    with Session(engine) as session:
        sentence = select(Categoria)
        registros = select(Categoria).order_by(Categoria.nome)
        print("Id, Nome, #produtos, Data cadastro, Data de modificacao")
        for categoria in registros:
            print(f"{categoria.id}, {categoria.nome}{len(categoria.lista_de_produtos)}, "
                  f"{categoria.dta_cadastro}, {categoria.dta_atualizacao}")


# def adicionar(engine: Engine):
#     with Session(engine) as session:
#         nome = input("Nome da categoria: ")
#         categoria = Categoria()
#         categoria.nome = nome
#         session.add(categoria)
#         try:
#             session.commit()
#         except:
#             print("Erro ao adicionar")
#         else:
#             print("Categoria adicionada com sucesso")



