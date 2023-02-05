<h1 align="center">Konia Project</h1>

<br>

### Project description

This project was created during a selection process offered by [Konia Tecnologia](https://konia.com.br/). The development of an API for registering and listing products was requested. The code was written in Python using the Django framework.

<br>

### Project status 👨‍💻 under development!

<br>

### Index

- [🛠️ Technologies used](#️-technologies-used)
- [📜 Documentation](#-documentation)
  - [Base URL](#base-url)
  - [Product](#product)
    - [Endpoints](#endpoints)
- [💻 Quick start](#-quick-start)
- [Author](#author)
- [License](#license)

<br>

## 🛠️ Technologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

<br>

## 📜 Documentation

### Base URL

https://under_development - (tip: add an endpoint at the end)

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
Host: under_development
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
  "id": "1",
  "name": "Steve Jobs - Walter Isaacson",
  "created_at": "2023-01-13T18:34:26.626Z"
}
```

<br>

<h3>👉 /konia_project/product</h3>

[back to Endpoints](#endpoints)

<h3>Request information</h3>

```
GET /konia_project/product
Host: under_development
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
    "id": "1",
    "name": "Walter Isaacson - Steve Jobs",
    "created_at": "2023-01-13T18:34:26.626Z"
  },
  {
    "id": "2",
    "name": "Josh Marlerman - Caixa de pássaros",
    "created_at": "2023-01-13T18:34:26.626Z"
  },
  {
    "id": "3",
    "name": "Aldous Huxley - Admirável mundo novo",
    "created_at": "2023-01-13T18:34:26.626Z"
  }
]
```

<br>

## 💻 Quick start

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
