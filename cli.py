from tree import Node_diretorio, sistema_arquivo

# Criando pasta mas mudar para outro arquivo para organizar
sistema = sistema_arquivo()
docs = Node_diretorio('Documentos')
img = Node_diretorio('Imagens')
sistema.raiz.sub_diretorios.extend([docs, img])

# Criando arquivos
docs.arquivos = ['doc1.txt', 'doc2.txt']
img.arquivos = ['img.txt', 'img2.txt']

sistema.run(sistema)
