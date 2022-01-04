# EncryptingCommunication
> EncryptingCommunication (nome nada criativo hahaha) é um script Python de criptografia de ponta a ponta baseada no método PBKDF2-SHA256, que conta com uma interface feita utilizando o módulo Built-in - Tkinter. 

EncryptingCommunication é um programa Python para criptografia que se baseada no método de SHA - Secure Hashinh Algorithm - para gerar Hashs baseadas em mensagens a partir do input do usuário, que só podem ser decodificadas utilizando a salt e master-key do mesmo. Para entender um pouco melhor sobre como o método [PBKDF2-SHA256](https://docs.python.org/3/library/hashlib.html) funciona você pode assistir um desses dois vídeos do canal Computerphile: [SHA: Secure Hashing Algorithm - Computerphile](https://www.youtube.com/watch?v=DMtFhACPnTY) e [Hashing Algorithms and Security - Computerphile](https://www.youtube.com/watch?v=b4b8ktEV4Bg).

## Instalação

### Linux:
```sh
which python3 //Para verificar se o Python está instalado
```

Caso o comando acima retorne algo como `which: no python in (...)` o seu Python não está instalado ainda. Agora, faça o seguinte para instalar o python, o pip e o git (se ainda não tiver).

Distros baseadas em Debian/Ubuntu:
```sh
sudo apt-get install python3 python3-pip git
```

Distros baseadas em RedHatLinux ou CentOs:
```sh
sudo yum install python3 python3-pip git
```

Clonando o repositórios e os arquivos:
```sh
git clone https://github.com/P-py/EncryptingCommunication.git

cd ./EncryptingCommunication
```

Seguindo para a instalação dos requisitos de módulos.
```sh
pip3 install -r requirements.txt
```

*Agora basta abrir os arquivos no seu editor de texto favorito e rodá-los, ou apenas executar direto do terminal com python main.py*

### Windows:
```sh
python --version //Para verificar se o Python está instalado
```

Caso o comando acima retorne um erro, o seu python provavelmente não está instalado, então siga os passos: https://python.org.br/instalacao-windows/

Também é importante que você possua o [git](https://git-scm.com/) instalado.

```sh
git clone https://github.com/P-py/EncryptingCommunication.git

cd ./EncryptingCommunication
```

Seguindo para a instalação dos requisitos de módulos.
```sh
pip3 install -r requirements.txt
```

*Agora basta abrir os arquivos no seu editor de texto favorito e rodá-los, ou apenas executar direto do terminal com python main.py*

## Exemplo de uso

![](https://github.com/P-py/EncryptingCommunication/blob/main/header0.PNG?raw=true)

## Configuração para Desenvolvimento

### Linux:
```sh
sudo apt-get install python3-pip python3 git

git clone https://github.com/P-py/EncryptingCommunication.git

cd ./EncryptingCommunication
```

## Histórico de lançamentos
* 0.1.0
    * Primeiro lançamento
    * MUDANÇA: Debugging na UI
    * ADD: Encrypt func
    * ADD: Decrypt func
* 0.0.1
    * Desenvolvimento
    * Wireframe básico

## Meta

Pedro – [@P-py](https://twitter.com/curliy1)

Distribuído sob a licença MITVeja `LICENSE` para mais informações.

[Saiba mais sobre mim clicando aqui](https://github.com/P-py/P-py)

## Contributing

1. Faça o _fork_ do projeto (https://github.com/P-py/EncryptingCommunication/fork)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_
