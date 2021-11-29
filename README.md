# Email Sender
This Project sends an email to the specified mail address when requested on the provided REST-API
The entire application is contained within `app.py`

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install components.

```bash
virtualenv venv
```

For OSX/Linux: 
```bash
source venv/bin/activate
```
For Windows: 
```bash
venv\scripts\activate
```

```bash
pip install Flask
```

## Excecute
To run the project
```bash
python app.py
```

## REST-API
API details to receive an email

## Hello World
Used to Print Hello World on Screen
**URL** : `/`
**Method** : `GET`

### Response
`Hello World`

About API:
1. "/" to print Hello World
2. "/emails" (Method = "POST") => 
