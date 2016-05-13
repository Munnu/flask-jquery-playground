# To run:
You need pip installed onto your system and also virtualenv
Go find them online if you don't have it.

virtualenv is useful when you don't want to install a bajillion
python modules inside of your actual computer

You need to create a virtual environment by doing something like
virtualenv <name_your_environment_folder>

Then once the environment is made do 
source <name_your_environment_folder>/bin/activate

load the dependencies by going:
pip freeze < requirements.txt

You need flask to work this.
If pip freeze doesn't work install flask by doing
pip install flask

# What's in this so far:
This application uses flask and what it does is it takes the user's input
that is submitted through the text forms and sends it over to python via
flask, then returns the user's input to the HTML frontend. Uses jQuery.
