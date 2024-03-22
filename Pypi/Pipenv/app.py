# pipenv install []
# pipenv --venv
# pipenv shell
# pipenv install
# pipenv install --ignore-pipfile

# pipenv graph
# pipenv uninstall []
# pipenv update --outdated
# pipenv update []
import requests


response = requests.get("https://www.google.com")
print(response)
