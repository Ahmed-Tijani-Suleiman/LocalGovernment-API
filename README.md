# State/Local Government crudapi


## Introduction
This Api will fetch all the local government for a given state. There are fours states in the database
1- Akwa Ibom, 2- Cross Rivers, 3- Rivers, 4- Bayelsa




## Tech Stack (Dependencies)

### 1. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **MSSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 *
You can download and install the dependencies mentioned above using `pip` as:
```
pip install virtualenv
pip install SQLAlchemy
pip install postgres
pip install Flask
pip install Flask-Migrate
```
 


## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models and controllers.
                    "python app.py" to run after installing dependencies
  ├── config.py *** Database URLs,
  ├
  ├
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├
  
      

Overall:
* Models are located in the `MODELS` section of `app.py`.
* Controllers are also located in `app.py`.


## Development Setup

1. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/Scripts/activate
```

2. **Install the dependencies:**
```
pip install -r requirements.txt
```

3. **Run the development server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py
```
```

6. **Verify on the Browser**<br>

Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

### Endpoints

#### GET '/api/lga/<stateId>'
- Fetches Department, Email, Staff_id.
 
- Sample: `GET http://127.0.0.1:5000/api/lga/1`
```
  
[
  {
    "id": 1,
    "name": "Abak",
    "state_id": 1
  },
  {
    "id": 2,
    "name": "Eastern Obolo",
    "state_id": 1
  },
  {
    "id": 3,
    "name": "Eket",
    "state_id": 1
  },
  {
    "id": 4,
    "name": "Esit Eket",
    "state_id": 1
  },
  {
    "id": 5,
    "name": "Essien Udim",
    "state_id": 1
  },
  {
    "id": 6,
    "name": "Etim Ekpo",
    "state_id": 1
  },
  {
    "id": 7,
    "name": "Etinan",
    "state_id": 1
  },
  {
    "id": 8,
    "name": "Ibeno",
    "state_id": 1
  },
  {
    "id": 9,
    "name": "Ibesikpo Asutan",
    "state_id": 1
  },
  {
    "id": 10,
    "name": "Ibiono Ibom",
    "state_id": 1
  },
  {
    "id": 11,
    "name": "Ika",
    "state_id": 1
  },
  {
    "id": 12,
    "name": "Ikono",
    "state_id": 1
  },
  {
    "id": 13,
    "name": "Ikot Abasi",
    "state_id": 1
  },
  {
    "id": 14,
    "name": "Ikot Ekpene",
    "state_id": 1
  },
  {
    "id": 15,
    "name": "Ini",
    "state_id": 1
  },
  {
    "id": 16,
    "name": "Itu",
    "state_id": 1
  },
  {
    "id": 17,
    "name": "Mbo",
    "state_id": 1
  },
  {
    "id": 18,
    "name": "Mkpat Enin",
    "state_id": 1
  },
  {
    "id": 19,
    "name": "Nsit Atai",
    "state_id": 1
  },
  {
    "id": 20,
    "name": "Nsit Ibom",
    "state_id": 1
  },
  {
    "id": 21,
    "name": "Nsit Ubium",
    "state_id": 1
  },
  {
    "id": 22,
    "name": "Obot Akara",
    "state_id": 1
  },
  {
    "id": 23,
    "name": "Okobo",
    "state_id": 1
  },
  {
    "id": 24,
    "name": "Onna",
    "state_id": 1
  },
  {
    "id": 25,
    "name": "Oron",
    "state_id": 1
  },
  {
    "id": 26,
    "name": "Oruk Anam",
    "state_id": 1
  },
  {
    "id": 27,
    "name": "Udung Uko",
    "state_id": 1
  },
  {
    "id": 28,
    "name": "Ukanafun",
    "state_id": 1
  },
  {
    "id": 29,
    "name": "Uruan",
    "state_id": 1
  },
  {
    "id": 30,
    "name": "Urue-Offong/Oruko",
    "state_id": 1
  },
  {
    "id": 31,
    "name": "Uyo",
    "state_id": 1
  }
]
   

```

#### POST '/staff''


