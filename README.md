# Prepaid-Recharge-API
Recharge-Application-with user authentication

Admin user :- vinaykushwaha@gloify.com Admin password :- 7879519773

At first clone this project- Install this module :- pip install virtualenv Then create virtual env. in which directory your project is cloned usig this command :- virtualenv env_name Then activate your virtual env after your dir :- .\env_name\Scripts\activate. Then go to project folder and run this command :- pip install -r requirements.txt.

Then run this command to run the project :- python manage.py runserver

Then....

POST http://127.0.0.1:8000/recharge/signup/ responsible for signup with name,email,mobile and password with post method.
POST http://127.0.0.1:8000/recharge/login/ responsible for signin with email and password and return a valid token with post method. 
GET http://127.0.0.1:8000/recharge/getplans/ responsible for get the all available palns with get method with a valid token because this is protected endpoint. 
POST http://127.0.0.1:8000/recharge/do/recharges/ responsible for do recharge as your given mobile number,valid operator, valid area/circle, valid plan with valid user token.


mobile -> valid 10 digit of mobile no.

valid operator -> Airtel Prepaid, BSNL Prepaid, Jio Prepaid, VI Prepaid, same as it is formate.

valid area/circle -> Andhra Pradesh & Telangana, Assam , Bihar & Jharkhand, others mention in model.

valid plan -> 499, 3359, 1799, 839, 838, 719, 699, 666, 599, 549, 455, 449, 359, 209, 256, 479, 299, 155, 179, 99, 239

plans are indicate what is the price of your paln.

Thanks................
