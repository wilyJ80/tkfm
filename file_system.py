def criacao_dic():
    import tree
    #Criando diretorio
    sistema = tree.sistema_arquivo()
    docs = tree.Node_diretorio('Documentos')
    img = tree.Node_diretorio('Imagens')
    sistema.raiz.sub_diretorios.extend([docs,img])


    #Criando arquivo
    docs.arquivos = ['doc1.txt', 'doc2.txt']
    img.arquivos = ['img.txt', 'img2.txt']

    return sistema