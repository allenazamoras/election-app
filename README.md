# Election App  
### Requirements
* Python (2.7 or higher)
* Django (1.10 or higher)
* Django REST Framework 3

---
### Installation  
```git clone https://github.com/boredchinese/election-app```

---
### Setup  
Install the following within a virtual environment  
```
pip install django
pip install djangorestframework
```
---
Move to the directory: ```/election-app/``` here you can find the ```manage.py``` file


( !! Be sure you are inside a virtual environment with Django and djangorestframework !! )  
( You can check for installed packages by typing ```$ pip freeze``` or ```$ pip list``` in the terminal )

---
Enter this command in the terminal:  
```
$ python manage.py runserver
```

If setup is successful you should see the following output in the terminal:
```
System check identified no issues (0 silenced).
May 07, 2018 - 07:49:23
Django version 2.0.5, using settings 'tutorial.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
_Note: The text may vary but you get the idea_

Open your browser and copy the link into the address bar, in this case it's  
```http://127.0.0.1:8000/``` or ```http://localhost:8000/```
