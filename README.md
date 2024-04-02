# Teamlist

![GitHub repo size](https://img.shields.io/github/repo-size/sandrofilho2000/teamlist?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/sandrofilho2000/teamlist?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/sandrofilho2000/teamlist?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/sandrofilho2000/teamlist?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/sandrofilho2000/teamlist?style=for-the-badge)

![image](https://github.com/sandrofilho2000/teamlist/assets/75636911/3e08d8b4-68c3-4f47-b5a5-75c18de0bd1d)

> Football almanac gathering data from over 100,000 players, 3,700 teams, and 250 leagues.

### Adjustments and Improvements

The project is still in development, and the next updates will focus on the following tasks:

- [x] Deploy on Google Cloud Service
- [x] Create stadium page
- [x] Associate trophies with teams
- [ ] Create player transfer page
- [ ] Retrieve additional player information

## 💻 Prerequisites

Before you start, make sure you meet the following requirements:

- You have installed the latest version of python on your machine

## ☕ Running Teamlist

To run Teamlist, follow these commands in the root directory after cloning the repository:

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

## 💻 Accessing the Django panel

To access the Django administrative panel, you first need to create a superuser. You can do this by running the following command:

```
python manage.py createsuperuse
```

After that, simply enter the desired username, password, and email in the terminal, access the path /admin, and log in.

## 🎨 Color System

Each of the teams, leagues, and countries has a unique color configuration determined by the item's image.

| Liverpool | Palmeiras | Boca Juniors |
|-----------|-----------|--------------|
| ![teamlist-fpfslipaga-uc a run app_teams_4_(iPhone 6_7_8)](https://github.com/sandrofilho2000/teamlist/assets/75636911/7465b0ff-0830-4cfd-9114-8edbf63c6d3d) | ![teamlist-fpfslipaga-uc a run app_teams_157_(iPhone 6_7_8) (1)](https://github.com/sandrofilho2000/teamlist/assets/75636911/b34f28bd-0258-4232-bdb7-f9ef8aac00db) | ![teamlist-fpfslipaga-uc a run app_teams_307_(iPhone 6_7_8) (1)](https://github.com/sandrofilho2000/teamlist/assets/75636911/71e465f3-1555-4830-a508-3344e556195d)


> After the user logs in, they have the option to edit the colors of the items through the color widget or through the panel as shown in the gif below:

![Animação](https://github.com/sandrofilho2000/teamlist/assets/75636911/ad41730d-f522-44fb-a7f3-f9be52805626)


## 📫 Contributing to Teamlist

To contribute to Teamlist, follow these steps:

1. Fork this repository.
2. Create a branch: git checkout -b <branch_name>.
3. Make your changes and commit them: `git commit -m '<mensagem_commit>'`
4. Push to the original branch: `git push origin Teamlist / <local>`
5. Create the pull request.

Alternatively, refer to the GitHub documentation on [how to create a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Contributors

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Leolupe/" title="Leandro Cardoso">
        <img src="https://avatars.githubusercontent.com/u/20233983?v=4" width="100px;" alt="Leandro Cardoso GitHub avatar"/><br>
        <sub>
          <b>Leandro Cardoso</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

