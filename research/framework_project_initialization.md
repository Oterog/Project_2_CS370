**instructions/process for project initiialization with this framework will go here.**

## TurboGears Fullstack Development:

### Small Scale "Minimal Mode" Setup (not fullstack):

```BASH
$ pip install TurboGears2
$ python myapp.py
```

### FullStack Solution with TurboGears devtools:

Install TurboGears devtools and create a new project:

```BASH
$ pip install tg.devtools
$ gearbox quickstart myproj
```

Install the project in editable mode and start the server:

```BASH
$ cd myproj
$ pip install -e .
$ gearbox serve
```

### References:

1. [TurboGears Documentation](https://www.turbogears.org/)
2. [TurboGears Minimal Mode](https://turbogears.readthedocs.io/en/latest/turbogears/minimal/index.html)
3. [TurboGears Fullstack Development](https://turbogears.readthedocs.io/en/latest/turbogears/wiki20.html)
4. [Fullstack Python](https://www.fullstackpython.com/turbogears.html)
5. [TurboGears Masterdoc](https://turbogears.readthedocs.io/en/latest/)



## Setting up the environment:

Virtual Environment:

#### Install: 

```BASH
pip install virtualenv
```

Can also do this instead:

```BASH
sudo apt install python3-virtualenv
```

Create/activate virtual environment with:
```BASH
$ virtualenv tgenv
$ . tgenv/bin/activate
```

then once active, install TurboGears:
```BASH
$ pip install TurboGears2
```

or
```BASH
 pip install tg.devtools
 ```
 FOR FULLSTACK!

 ```BASH
 gearbox quickstart app
 ```

 ```BASH
cd app
```

```BASH
gearbox serve
```