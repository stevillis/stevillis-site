# A Portfolio to show some IT courses I studied

## About the site

The site was created using Django, PostgreSQL and Tailwind CSS. It has a public page that shows Courses, Formations and
some information about me. Using Django Admin I created the Models where I can register the information about the
courses and Formations that allows me to update the site content dinamically.

## The Entity Relationship Diagram

![Entity Relationship Diagram](https://github.com/stevillis/stevillis-site/blob/master/DER/DER.jpg?raw=true)

## Development instructions

### Translation

1. Generate translations

```shell
$ python manage.py makemessages -l pt_BR -i venv
$ python manage.py makemessages -l en -i venv
```

2. Edit the .po files with Poedit

3. Compile the translations

```shell
$ python manage.py compilemessages
```

---

### Customize Tailwind CSS

Compile modifications on tailwind.config.js file

```shell
$ npx tailwindcss build -i style.css -o dist/my-site.css
```

---

### Coding Style fixing by custom django command

Fix import ordering with isort and show some warnings about the code with flake8 on the console

```shell
$ python manage.py cleancode
```

---