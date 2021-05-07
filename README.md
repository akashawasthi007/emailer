# emailer

This is a mini project used to send mails one at a time or many.

**prerequisites**

python3
django3.2

**how to use...**

first of all open settings.py file in emailer and edit the line 22 where you have to put your email which
you will use for sending mails.

now edit the line 23 where you have to put your email password 

and at last edit you settings from your email accoun -> set on to allow less secure apps 
from <a href="https://myaccount.google.com/lesssecureapps?gar=1&pli=1&rapt=AEjHL4MDp9Q9E6GbbXFUBY14Znk6zaNJiEY4DoTFkTYppB2Lt48Du4ze0xj2lQb38cCpfcXZ1NosaClnT2DqFRkHRQNXeJLstg">gmail/login/settings/security/allow_less_secure_apps</a>

**steps to run**

python manage.py migrate
python manage.py makemigration emailer_app
python manage.py migrate
python manage.py runserver

then copy and paste the localhost link in your browser

**preview**
![gg](https://user-images.githubusercontent.com/50840565/117471512-8dcd2b80-af75-11eb-866b-ec94108b6483.png)
