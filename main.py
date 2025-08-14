from sqlalchemy import create_engine

import app_categorias
import app_produtos
from config import read_config

if __name__ == '__main__':
    config = read_config()
    engine = create_engine(url=config.url_bd, echo=False)

    while True:
        print("MENU")
        print("============================")
        print ("1. Listar Categorias")
        print ("2. Adicionar Categoria")
        print ("3. Modificar Categoria")
        print ("4. Deletar Categoria")
        print ("5. Listar Produtos")
        print ("6. Adicionar Produto")
        print ("7. Modificar Produto")
        print ("8. Deletar Produto")
        print ("0. Finalizar")

        opcao = input("Digite a opção desejada: ")
        match opcao:
            case "0":
                exit()
            case "1" :
                app_categorias.listar(engine)
            case "2" :
                app_categorias.adicionar(engine)
            case "3" :
                app_categorias.modificar(engine)
            case "4" :
                app_categorias.deletar(engine)
            case "5" :
                app_produtos.listar(engine)
            case "6" :
                app_produtos.adicionar(engine)
            case "7" :
                app_produtos.modificar(engine)
            case "8" :
                app_produtos.deletar(engine)
