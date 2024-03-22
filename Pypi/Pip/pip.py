# pip install requests
# pip install --upgrade pip
# pip list
# pip install requests==2.9.0
# pip install requests==2.9.*
# pip uninstall requests

# pip install requests~=2.9.0
import requests


response = requests.get("https://www.google.com")
print(response)
