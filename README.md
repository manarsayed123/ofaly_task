# ofaly_task
instructions to get application running
1-create virtual environment through this command "virtualenv env"
2- activate environment using this command " source env/bin/activate" #this command for linux if windows check the activation command for windows
3-run this command "pip install -r requirements.txt"
then run application using this command " uvicorn main:app --reload"

the api url is http://127.0.0.1:8000/?city=cairo&country=egypt  # added city and country as an example  use any values do you need
this is the curl    curl --location --request GET 'http://127.0.0.1:8000/?city=cairo&country=egypt'

Note i attached the secret key for weather api to enable you for using it for more security this key must be on environmental variables .


