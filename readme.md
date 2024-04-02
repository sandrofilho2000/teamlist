# Nome do projeto

![GitHub repo size](https://img.shields.io/github/repo-size/sandrofilho2000/teamlist?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/sandrofilho2000/teamlist?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/sandrofilho2000/teamlist?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/sandrofilho2000/teamlist?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/sandrofilho2000/teamlist?style=for-the-badge)

<img src="teamlist.png" alt="Exemplo imagem">

> Almanaque futebolístico que reúne dados de mais de 100.000 jogadores, 3.700 equipes e 250 ligas.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Realizar deploy na Google Cloud Service
- [x] Criar página de estádios
- [x] Relacionar troféus à equipes
- [ ] Criar a página de transferências de jogadores
- [ ] Buscar informações adicionais de jogadores

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente do `python` em sua máquina

## ☕ Rodando o Teamlist

Para rodar Teamlist, siga estas etapas após clonar o repositório:

```
python venv -m venv
```

```
pip install requirements.txt
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```

## 💻 Acessando o painel do Django

## 📫 Contribuindo para Teamlist

Para contribuir com Teamlist, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin Teamlist / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://avatars3.githubusercontent.com/u/31936044" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Iuri Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://s2.glbimg.com/FUcw2usZfSTL6yCCGj3L3v3SpJ8=/smart/e.glbimg.com/og/ed/f/original/2019/04/25/zuckerberg_podcast.jpg" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Mark Zuckerberg</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="defina o titulo do link">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 😄 Seja um dos contribuidores

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.