# [ Python-Blog]()


## Description
The user can register and create an account where they will have the ability to login and create new posts and post them, they can also update their posts and also delete the same post. The user has an option of updating their profile by uploading their photos.

## BDD

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Registratin | Fill in the form in the registration page | Redirects to the login page |
| Login | Fill in the form in the create new blogs | Redirects to the home page with blog posts |
| Posting blogs | In the home page, enter your pitch in text, select a category in the drop down menu and hit Pitch It Button! | Reloads the page with the pitch as the newest pitch |
| Updating and deleting blogs | Click the update button in the profile page or the delete button | Redirects the user to the updated blog or deletes the chosen blog |
| Updating profile picture | Click the select button then the update button | Redirects the user to where the photo is then automatically updates when the user clicks on the update button |


## Live link


## Set-up and Installation

### Prerequsites
    - Python 3.7
    - Ubuntu software

### Clone the Repo
Run the following command on the terminal:
``

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.7 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Known bugs

```None so far but i'll be glad to be communicated to if there is one ```


## Technologies used
    - Python 3.7
    - HTML
    - Bootstrap 
    - Animate CSS
    - Heroku
    - Postgresql

## Support and contact details
Contact me on salemowino18@gmail.com for any comments, reviews or advice.

### License
Copyright (c) **Salem**