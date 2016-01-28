flask-restful-example
=====================


pip install -r requirements.txt
python manage.py createdb

python run.py
python manage.py test



curl -i -H "Content-Type: application/json" -H -X POST -d "{\"type\": \"simple\", \"user\": \"user\", \"pswd\": \"q\"}" http://127.0.0.1:5000/api/v1/auth/signin
