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
        """
        função para listar os arquivos e diretorios daquela parte
        """
        print('Conteúdo de', self.atual.nome)
        for subdiretorio in self.atual.sub_diretorios:
            print('{}/ (diretorio)'.format(subdiretorio.nome))
        for arquivo in self.atual.arquivos:
            print('arquivo: {}'.format(arquivo))

    def cd(self, nome):
        """
        função para voltar um diretorio ou voltar 2
        """
        if nome == '..':
            self.mover_diretorio(1)
        elif nome == '../..':
            self.mover_diretorio(2)
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

    def mover_diretorio(self, nivel):
        """
        função usada para voltar os diretorios
        """
        if nivel == 0:
            return
        if nivel == 1:
            if self.historico:
                self.atual = self.historico.pop()
            else:
                print("Já está no diretório raiz")
        else:
            if self.historico:
                self.historico.pop()
                self.mover_diretorio(nivel - 1)
            else:
                print("Já está no diretório raiz")

    def mkdir(self, nome_pasta, dir=None, nivel=2):
        """
        função para criar pasta no diretorio atual ou especificando um caminho
        """
        if nivel == 2:
            caracter_especial = ['!', '@', '#', '$', '%', '^', '&', '*',
                                 '(', ')', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
            if any(caracter in nome_pasta for caracter in caracter_especial):
                print(
                    'Nome de pasta não pode conter caracteres especiais. Exemplo: ! @ # / : >')
            elif nome_pasta:
                novo_diretorio = Node_diretorio(nome_pasta)
                self.atual.sub_diretorios.append(novo_diretorio)
                print('Pasta {} criada com sucesso em {}'.format(
                    nome_pasta, self.atual.nome))
        elif nivel == 3:
            caracter_especial = ['!', '@', '#', '$', '%', '^', '&', '*',
                                 '(', ')', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
            if any(caracter in nome_pasta for caracter in caracter_especial):
                print(
                    'Nome de pasta não pode conter caracteres especiais. Exemplo: ! @ # / : >')
            elif dir:
                partes = dir.split('/')
                diretorio_atual = self.raiz
                for parte in partes:
                    encontrado = False
                    for subdiretorio in diretorio_atual.sub_diretorios:
                        if subdiretorio.nome.lower() == parte.lower():
                            diretorio_atual = subdiretorio
                            encontrado = True
                            break
                    if not encontrado:
                        print('Diretório {} não encontrado'.format(parte))
                        return
                novo_diretorio = Node_diretorio(nome_pasta)
                diretorio_atual.sub_diretorios.append(novo_diretorio)
                print('Pasta {} criada com sucesso em {}'.format(
                    nome_pasta, diretorio_atual.nome))
            else:
                print('Caminho não especificado')

    def touch(self, nome_arquivo):
        """
        função para criar arquivo
        """
        caracter_especial = ['!', '@', '#', '$', '%', '^', '&', '*',
                             '(', ')', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '<', '>', '/', '?']
        if any(caracter in nome_arquivo for caracter in caracter_especial):
            print(
                'Nome de pasta não pode conter caracteres especiais. Exemplo: ! @ # / : >')
        else:
            if nome_arquivo:
                self.atual.arquivos.append(nome_arquivo)
                print('Arquivo {} criado com sucesso' .format(nome_arquivo))
            else:
                pass

    def mv(self, nome_origem, novo_nome):
        """
        função para renomear arquivo
        """
        encontrado = False
        for i, arquivo in enumerate(self.atual.arquivos):
            if arquivo == nome_origem:
                self.atual.arquivos[i] = novo_nome
                print('Arquivo {} renomeado para {}'.format(
                    nome_origem, novo_nome))
                encontrado = True
                break
        if not encontrado:
            print('Arquivo não encontrado: {}'.format(nome_origem))

    def rm(self, nome_arquivo):
        """
        função para deletar arquivo
        """
        encontrado = False
        for arquivo in self.atual.arquivos:
            if arquivo == nome_arquivo:
                self.atual.arquivos.remove(arquivo)
                print('Arquivo {} removido'.format(nome_arquivo))
                encontrado = True
                break
        if not encontrado:
            print('Arquivo não encontrado: {}'.format(nome_arquivo))

    def print_tree(self, node, prefix=""):
        result = ""
        for subdir in node.sub_diretorios:
            result += prefix + "|-- " + subdir.nome + "/"
            result += self.print_tree(subdir, prefix + "|   ")
        for arquivo in node.arquivos:
            result += prefix + "|-- " + arquivo
        return result

    def tree(self):
        print(self.atual.nome, '/')
        self.print_tree(self.atual)

    def execute_command(self, comando):
        output = []

        if comando == 'ls':
            output.append('Conteúdo de ' + self.atual.nome)
            for subdiretorio in self.atual.sub_diretorios:
                output.append('{}/ (diretorio)'.format(subdiretorio.nome))
            for arquivo in self.atual.arquivos:
                output.append('arquivo: {}'.format(arquivo))

        elif comando.startswith('cd'):
            partes = comando.split()
            if len(partes) == 2:
                self.cd(partes[1].capitalize())
                output.append('Mudou para diretório {}'.format(partes[1]))
            else:
                output.append('Uso: cd <diretorio>')

        elif comando.startswith('mkdir'):
            partes = comando.split()
            if len(partes) == 2:
                self.mkdir(partes[1].capitalize(), None, 2)
            elif len(partes) == 3:
                self.mkdir(partes[1].capitalize(),
                           partes[2].capitalize(), 3)
            else:
                output.append('Uso: mkdir <nome da pasta>')

        elif comando.startswith('touch'):
            partes = comando.split()
            if len(partes) == 2:
                self.touch(partes[1].capitalize())
            else:
                output.append('Uso: touch <nome do arquivo>')

        elif comando.startswith('mv'):
            partes = comando.split()
            if len(partes) == 3:
                self.mv(partes[1].capitalize(),
                        partes[2].capitalize())
            else:
                output.append(
                    'Uso: mv <nome do arquivo que quer alterar>  <nome do novo arquivo>')

        elif comando.startswith('rm'):
            partes = comando.split()
            if len(partes) == 2:
                self.rm(partes[1].capitalize())
            else:
                output.append('Uso: rm <nome do arquivo que quer excluir>')

        elif comando == 'tree':
            output.append(self.print_tree(self.atual, ''))

        elif comando == 'help':
            output.append("Comandos:")
            output.append("ls | cd | mkdir | touch | mv | rm | tree | exit")

        elif comando == 'exit':
            output.append('Saindo do sistema')
            return output, True

        else:
            pass

        return "\n".join(output), False
