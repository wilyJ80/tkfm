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
                if subdiretorio.nome == nome:
                    self.historico.append(self.atual)
                    self.atual = subdiretorio
                    encontrado = True
                    break
            if not encontrado:
                print('diretório não encontrado')

    def mkdir(self):
        caracter_especial = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
        nome_pasta = input('Digite o nome da pasta que voce quer criar: ')
        if any(caracter in nome_pasta for caracter in caracter_especial):
            print('Nome de pasta não pode conter caracteres especiais. Exemplo: ! @ # / : >')
        elif nome_pasta:
            novo_diretorio = Node_diretorio(nome_pasta)
            self.atual.sub_diretorios.append(novo_diretorio)
            print('Pasta {} criada com sucesso em {}'.format(nome_pasta, self.atual.nome))

    def diretorio_pai(self, diretorio_atual, diretorio_alvo, pai=None):
        if diretorio_atual == diretorio_alvo:
            return pai

        for subdiretorio in diretorio_atual.sub_diretorios:
            resultado = self.diretorio_pai(subdiretorio, diretorio_alvo, diretorio_atual)
            if resultado is not None:
                return resultado

        return None

# Criando diretorio
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
                sistema.cd(partes[1])
            else:
                print('Uso: cd <diretorio>')
        elif comando == 'mkdir':
            sistema.mkdir()
        elif comando == 'exit':
            print('Saindo do sistema')
            break
        else:
            pass
