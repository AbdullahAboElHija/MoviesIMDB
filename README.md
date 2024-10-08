### How to Run the Project

Follow these steps to set up and run the project locally:

#### 1. Clone the Repository
Open a terminal and run the following command to clone the repository:
git clone https://github.com/AbdullahAboElHija/MoviesIMDB.git

cd MoviesIMDB

#### 3. Create a Virtual Environment
It's recommended to use a virtual environment for managing dependencies. Run the following command to create one:
python3 -m venv venv


#### 4. Activate the Virtual Environment
venv\Scripts\activate

#### 5. Install the Dependencies
Once the virtual environment is activated, install the required packages by running:
pip install -r requirements.txt

#### 6. Apply Migrations
Run Django migrations to set up the database:
python manage.py migrate


#### 7. Run the Development Server
Start the Django development server:
python manage.py runserver

#### 8. Access the Application
Once the server is running, open your web browser and go to:
http://127.0.0.1:8000/



### Main Screen
![Screenshot_2.png](Screenshot_2.png)

### Details Screen (reviews on film)

![Screenshot_1.png](Screenshot_1.png)


