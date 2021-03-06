[![Build Status](https://travis-ci.org/SendiSteve/My-Diary.svg?branch=cp2)](https://travis-ci.org/SendiSteve/My-Diary)
[![Coverage Status](https://coveralls.io/repos/github/SendiSteve/My-Diary/badge.svg)](https://coveralls.io/github/SendiSteve/My-Diary)
[![Maintainability](https://api.codeclimate.com/v1/badges/05dc968bdbd26eb874f5/maintainability)](https://codeclimate.com/github/SendiSteve/My-Diary/maintainability)

# MyDiary API
This is an api for MyDiary built with the python flask framework. It allows users to pen down their entries they wish to accomplish.

This API is live and hosted on [heroku](https://mydiarypro.herokuapp.com/)

## Technologies
1. Python 3.6.4
2. Flask==1.0.2
3. Virtualenv

## Getting Started
These following instructions will help to set up the application on a local development machine.

1. Clone the repository
```
https://github.com/SendiSteve/My-Diary.git```
```

2. Navigate to the repository
```
cd My-Diary
``` 

3. Create a virtual environment
```
virtualenv venv
```

4. Activate the virtual environment
```
source venv/bin/activate
```

5. Install dependencies
```
pip install -r requirements.txt
```

6. Run the application 
```
python run.py 
```

## Testing
To run tests 
1. Run tests
```
# in root directory

pytest
```

## API End points

Test the endpoints below using Postman


| End Point                      | Method        |   Functionality               |   Functionality  |
| -----------------------------  | ------------- | -------------------------     | ---------------- |    
| `/api/v1/entries`           |  GET       | User can GET all entries      | PUBLIC          |
| `/api/v1/entries`           |  POST       | User can ADD all entries      | PUBLIC          |
| `/api/v1/entries/<int:entry_id>`| DELETE | User can DELETE an entry by its id  | PUBLIC         |
| `/api/v1/entries/<int:entry_id>`| PUT    | User can UPDATE an entry by its id  | PUBLIC          |
