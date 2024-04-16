from collections import deque

class Node_diretorio:
    def __init__(self, nome):
        self.nome = nome
        self.sub_diretorios = []
        self.arquivos = []


class sistema_arquivo:
    def __init__(self):
        self.raiz = Node_diretorio('/')
        self.atual = self.raiz
        self.historico = []

    def ls(self):
        print('Conteúdo de', self.atual.nome)
        for subdiretorio in self.atual.sub_diretorios:
            print('{}/ (diretorio)'.format(subdiretorio.nome))
        for arquivo in self.atual.arquivos:
            print('arquivo: {}'.format(arquivo))

    def cd(self, nome):
        if nome == '..':
            if self.historico:
                self.atual = self.historico.pop()
                print("Diretório atual depois:", self.atual.nome)
            else:
                print("Já está no diretório raiz")
        else:
            encontrado = False
            for subdiretorio in self.atual.sub_diretorios:
                if subdiretorio.nome.lower() == nome.lower():
                    self.historico.append(self.atual)
                    self.atual = subdiretorio
                    encontrado = True
                    break
            if not encontrado:
                print('diretório não encontrado')

    def mkdir(self,nome_pasta):
        caracter_especial = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
        if any(caracter in nome_pasta for caracter in caracter_especial):
            print('Nome de pasta não pode conter caracteres especiais. Exemplo: ! @ # / : >')
        elif nome_pasta:
            novo_diretorio = Node_diretorio(nome_pasta)
            self.atual.sub_diretorios.append(novo_diretorio)
            print('Pasta {} criada com sucesso em {}'.format(nome_pasta, self.atual.nome))

    #problema criar com a extensão do arquivo
    def touch(self,nome_arquivo):
        caracter_especial = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '<', '>', '/', '?']
        if any(caracter in nome_arquivo for caracter in caracter_especial):
            print('Nome de pasta não pode conter caracteres especiais. Exemplo: ! @ # / : >')
        else:
            if nome_arquivo:
                self.atual.arquivos.append(nome_arquivo)
                print('Arquivo {} criado com sucesso' .format(nome_arquivo))
            else:
                pass

    def mv(self,nome_arquivo,novo_nome_arquivo):
        pass




# Criando pasta mas mudar para outro arquivo para organizar
sistema = sistema_arquivo()
docs = Node_diretorio('Documentos')
img = Node_diretorio('Imagens')
sistema.raiz.sub_diretorios.extend([docs, img])

# Criando arquivos
docs.arquivos = ['doc1.txt', 'doc2.txt']
img.arquivos = ['img.txt', 'img2.txt']



if __name__ == "__main__":
    while True:
        comando = input('Diretorio atual {} Digite o comando: '.format(sistema.atual.nome))
        if comando == 'ls':
            sistema.ls()

        elif comando.startswith('cd'):
            partes = comando.split()
            if len(partes) == 2:
                sistema.cd(partes[1].capitalize())
            else:
                print('Uso: cd <diretorio>')

        elif comando.startswith('mkdir'):
            partes = comando.split()
            if len(partes) == 2:
                sistema.mkdir(partes[1].capitalize())
            else:
                print('Uso: mkdir <nome da pasta>')
        
        elif comando.startswith('touch'):
            partes = comando.split()
            if len(partes) == 2:
                sistema.touch(partes[1].capitalize())
            else:
                print('Uso: touch <nome do arquivo>')

        elif comando.startswith('mv'):
            partes = comando.split()
            if len(partes) == 3:
                sistema.mv(partes[1].capitalize(), partes[2].capitalize())
                pass
            else:
                pass

        elif comando == 'exit':
            print('Saindo do sistema')
            break

        else:
            pass
