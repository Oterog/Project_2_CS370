Project documentation will go here
# Project 2 CS370
---
## Contributors: 
- **Stephanie Myalik**
- **Gabriel Otero**
---
## Getting started

---
## Project Description

---
## Project Objectives

---
## Project Structure 

---
## Problems Encountered

---

## Project initialization, running the application:

## Setting up the environment:

#### Virtual Environment:

Install: 

Install virtual environment: ``sudo apt install python3.10-venv``

Create virtual environment with: ``python3 -m venv venv``

Activate:
``. venv/bin/activate``

When you are done with the venv you can deactivate it with: ``` deactivate``` and then reactivate it with the same command as above.


#### Once the venv is active, install TurboGears:

```BASH
 pip install tg.devtools
```
dont run this, this is for initiallizing the app. already done. : ``gearbox quickstart turbogearsApp``
 

 ```BASH
cd turboGearsApp
```


install dependancies:

```BASH 
pip install -e . 
```


DOWNGRADE SQLALCHEMY ``pip install "sqlalchemy<2.0"`` wont serve otherwise

```BASH
gearbox serve
```