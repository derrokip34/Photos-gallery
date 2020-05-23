# PHOTOS GALLERY

## AUTHOR
- [Derrick Kiprop](https://github.com/derrokip34)

## PROJECT DESCRIPTION
This is a django app where a user can view images, search for images based on categories, see images from different location and copy links to the images

## SETUP AND USAGE INSTRUCTIONS
### Prerequisites
- A web browser
- Github account
- Terminal
- Python3.6
- Text editor software

#### Clone or download the zip file of this repository
- Clone by typing in the following command `git clone https://github.com/derrokip34/Photos-gallery.git`
- If you've downloaded the zip extract it in your preferred destination

#### Navigate into the project directory

#### Install python3.6 if not yet installed

##### Install virtual environment by typing the following command
`python3.6 -m venv --without-pip virtual`

#### Activate virtual environment
`source virtual/bin/activate`

#### Install pip
`curl https://bootstrap.pypa.io/get-pip.py | python`

#### Install dependencies by typing the following command
`pip install -r requirements.txt`

#### Create an `.env` file and edit it where appropriate
```bash
export SECRET_KEY=<your secret key>
export DB_NAME=<your database name>
export DB_USER=<your database username>
export DB_PASSWORD=<your database password>
export DEBUG=<True or False>
```
#### Run the following commands in your terminal
```bash
source .env
python3.6 manage.py runserver
```

#### Open 'http://127.0.0.1:8000/' in your browser and enjoy your app

## [BLOG Live site](https://gallery-3.herokuapp.com/)

## BDD
### Input required
- Category in search form
- Click copy link button

### Behaviour
- The app will search for images under the category typed
- The app will copy the image link the clipboard

### Output
- The app will display images under the category typed
- The link will be copied to the clipboard

## TECHNOLOGIES USED
- HTML
- CSS
- Bootstrap 4
- Material Design Bootstrap
- Python3.6
- Django
- Markdown
- Heroku
- PostgreSQL

## BUGS
There are no known bugs at the moment
In case of any bugs contact me at derrickip34@gmail.com

## LICENSE & COPYRIGHT INFORMATION
[MIT License](https://github.com/derrokip34/Photos-gallery/blob/master/license.md)
