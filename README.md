# Prepaid-Recharge-API
Recharge-Application-with user authentication

Admin user :- manojsoni.bhu@gmail.com Admin password :- 7879519773

At first clone this project- Install this module :- pip install virtualenv Then create virtualenv in which directory your project is cloned usig this command :- virtualenv env_name Then activate your virtual env after your dir :- .\env_name\Scripts\activate. Then go to project folder and run this command :- pip install -r requirements.txt.

Then run this command to run the project :- python manage.py runserver

Then....

POST http://127.0.0.1:8000/recharge/signup/ responsible for signup with name,email,mobile and password with post method.
POST http://127.0.0.1:8000/recharge/login/ responsible for signin with email and password and return a valid token with post method. 
GET http://127.0.0.1:8000/recharge/getplans/ responsible for get the all available palns with get method with a valid token because this is protected endpoint. 
POST http://127.0.0.1:8000/recharge/do/recharges/ responsible for do recharge as your given mobile number,valid operator, valid area/circle, valid plan with valid user token.


mobile -> valid 10 digit of mobile no.

valid operator -> Airtel Prepaid,Jio Prepaid, BSNL Prepaid, VI Prepaid, same as it is formate.

valid area/circle -> Andhra Pradesh & Telangana ,Assam ,Bihar & Jharkhand ,Chennai ,Delhi & NCR ,Gujrat ,Haryana ,Himanchal Pradesh ,
Jammu & Kashmir ,Karnataka ,Kerala ,Kolkata ,Madhya Pradesh & Chhattisgarh ,Maharashtra & Goa ,Mumbai ,North East ,Odisha ,Punjab ,
Rajasthan ,Tamil Nadu ,Uttar Pradesh East Uttar Pradesh West & Uttarakhand ,West Bengalmention in model.

# valid plan -> 119, 149, 179, 199, 209, 239, 249, 259, 296, 299, 479, 666, 719, 749, 419, 201, 555, 15, 25, 61, 121, 181, 241, 222, 2879, 2545, 75, 91, 125, 152, 186, 86

plans are indicate what is the price of your paln.

Thanks................
