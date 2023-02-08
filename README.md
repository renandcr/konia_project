<h1 style="color: #132A43; text-align: center">Konia Project</h1>

### Project description

This project was developed during a selection process offered by Konia Tecnologia. The development of an API for registering and listing products was requested. The API code was written in Python using the Django framework. An interface developed in React.js was also required. The interface is a complement to the API, it has a main screen where all the products that are saved in the database are rendered, in addition to a button for inserting new products. [Access the INTERFACE repository by clicking here](https://github.com/renandcr/konia_project_interface).

<br>

![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/renandcr/konia_project)
![Python version](https://img.shields.io/badge/python-3.10.4-yellow)
![Ubuntu version](https://img.shields.io/badge/ubuntu-20.04.5-green)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/renandcr/konia_project)
![GitHub repo size](https://img.shields.io/github/repo-size/renandcr/konia_project)
![GitHub top language](https://img.shields.io/github/languages/top/renandcr/konia_project)
![GitHub language count](https://img.shields.io/github/languages/count/renandcr/konia_project)
![GitHub](https://img.shields.io/github/license/renandcr/konia_project)

<br>

### Project status 👨‍💻 under development!

<br>

### Index

- [Technologies used](#️-technologies-used)
- [Documentation](#-documentation)
  - [Base URL](#base-url)
  - [Product](#product)
    - [Endpoints](#endpoints)
- [Author](#author)
- [License](#license)

<br>

## 🛠️ Technologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

### Auxiliary tools
- [Project Trello](https://trello.com/invite/b/1VBcO23u/ATTIc26549b84c8f528cf7fe584695dcacc570D29B69/konia-project)

<br>

## 📜 Documentation

### Base URL

http://localhost:8000 - (tip: add an endpoint at the end)

<br>

### Product

#### Endpoints

[back to index](#index)
| Method | Route | Description |
| ------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| POST | /konia_project/product | Create product. |
| GET | /konia_project/product | View products. |

<br>

<h3>👉 /konia_project/product</h3>

[back to Endpoints](#endpoints)

<h3>Request information</h3>

```
POST /konia_project/product
Host: localhost:8000
Content-type: application/json
```

<h3>Request body</h3>

```json
{
  "name": "Steve Jobs - Walter Isaacson"
}
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
201 Created
```

```json
{
  "id": 1,
  "name": "Walter Isaacson - Steve Jobs",
  "created_at": "2023-02-05T23:41:52.908114Z"
}
```

<br>

<h3>Response returned for product name already existing in database</h3>

Status code

```
400 Bad Request
```

```json
{
  "name": ["product with this name already exists."]
}
```

<br>

<h3>👉 /konia_project/product</h3>

[back to Endpoints](#endpoints)

<h3>Request information</h3>

```
GET /konia_project/product
Host: localhost:8000
```

<br>

<h3>Response returned for successful request</h3>

Status code

```
200 OK
```

```json
[
  {
    "id": 1,
    "name": "Walter Isaacson - Steve Jobs",
    "created_at": "2023-02-05T23:41:52.908114Z"
  },
  {
    "id": 2,
    "name": "Josh Malerman - Caixa de pássaros",
    "created_at": "2023-02-05T23:42:53.742201Z"
  },
  {
    "id": 3,
    "name": "Aldous Huxley - Admirável mundo novo",
    "created_at": "2023-02-05T23:43:30.181513Z"
  }
]
```

<br>

## Author

<h4><img alt="Foto de perfil" src="assets/readme/images/profile_photo_2.JPG" style="width: 100px; border-radius: 50px"/></h4>
Renan Ribeiro 🚀

<br>

<br>

Made with ❤️ by Renan Ribeiro 👋 Get in touch!

![WHATSAPP](<https://img.shields.io/badge/+55(43)996935385-25D366?style=flat-square&logo=whatsapp&logoColor=white>)
![GMAIL](https://img.shields.io/badge/renandcribeiro@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)
<a href="https://www.linkedin.com/in/renandcr">
<img src="https://img.shields.io/badge/Renan-0077B5?style=flat-square&logo=linkedin&logoColor=white"/></a>

<br>

## License

Licensed under [MIT](https://github.com/renandcr/konia_project/blob/development/LICENSE.md).
