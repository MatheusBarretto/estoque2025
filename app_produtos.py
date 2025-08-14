from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from app_categorias import selecionar_categoria
from models import Produto
from decimal import *

def listar(engine: Engine):
    with Session(engine) as session:
        sentenca = select(Produto).order_by(Produto.nome)
        registros = session.execute(sentenca).scalars()
        print("Id, Nome, Preco, Estoque, Ativo, Nome Categoria, Data cadastro, Data de modificacao")
        for produto in registros:
            print(f"{produto.nome}, {produto.preco}, "
                  f"{produto.estoque}, {"Ativo" if produto.ativo else "Inativo"}, {produto.categoria.nome}, "
                  f"{produto.dta_cadastro}, {produto.dta_atualizacao}")


def adicionar(engine: Engine):
    with Session(engine) as session:
        p = Produto()
        p.nome = input("Qual o nome do produto? ")
        p.preco = Decimal(input("Qual o preco do produto? R$: "))
        p.estoque = int(input("Qual o estoque inicial do produto?: "))
        x = input("O Produto está ativo? (S/N): ").lower()
        p.ativo = True if x[0] == "s" else False
        print("Selecione a categoria do produto")
        p.categoria = selecionar_categoria(session)
        session.add(p)
        try:
            session.commit()
        except:
            print("Erro na categoria")
        else:
            print("Produto adicionado com sucesso!")





