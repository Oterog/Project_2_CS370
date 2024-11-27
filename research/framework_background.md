# Project Research

## Table of Contents

- [What is TurboGears?](#what-is-turbogears)

- [TurboGears History](#turbogears-historytimeline)

- [Turbogears Features](#turbogears-features)

    - [SQLAlchemy](#sqlalchemy)

    - [Pylons](#pylons)

    - [Genshi](#genshi)

    - [Mako](#mako)

- [TurboGears Use Case](#turbogears-use-cases)

    - [Full-Stack Web Development](#full-stack-web-development)

    - [APIs and Microservices](#apis-and-microservices)

    - [Data-Intensive Applications](#data-intensive-applications)

    - [Prototyping and Rapid Development](#prototyping-and-rapid-development)

    - [Real-Time Web Applications](#real-time-web-applications)

    - [Agile Development](#agile-development)

### What is TurboGears?

- TurboGears is a fullstack web application framework for Python that is built on top of several other libraries and tools such as SQLAlchemy, Genshi, and Repoze.

- TurboGears is designed to be a flexible and extensible framework that allows developers to build web applications quickly and easily, while still providing the power and flexibility needed for more complex projects.

### TurboGears History/Timeline

#### 2005 – Creation of TurboGears

- TurboGears was first released in 2005 by Kevin Dangoor. It was born out of the need for a more powerful and flexible web framework for Python.

#### 2006 – TurboGears 1.0 Released

- TurboGears 1.0 was officially released. At the time, it stood out due to its integration with multiple libraries, like SQLAlchemy and Genshi.

#### 2007 – TurboGears Gains Popularity

- TurboGears began to gain attention in the Python web development community, particularly for its ability to integrate with existing Python libraries and frameworks.

#### 2010 – TurboGears 2.0 Final Release

- The release of TurboGears 2.0 was announced as a complete rewrite of the framework, aiming to offer better flexibility and extend the framework's scope.

- One of the key changes was the introduction of Pylon components and WebOb, a toolset for building web applications.

#### 2024 - TurboGears Today

- TurboGears remains a viable option for full-stack development in Python, particularly for developers who prefer flexibility and modularity.

- However, frameworks like Django, Flask, and newer asynchronous frameworks like FastAPI have become more prominent in the Python web development ecosystem.

### TurboGears Features

#### SQLAlchemy

- TurboGears uses SQL Alchemy to provide Database Scalability. Allowing automatic branching and minimizing to the number of inserts sent to the database. Also supporting eager and lazy loading of objects. 

#### Pylons

- TurboGears uses a system called 'Pylons' which is WSGI to object wrapper. Pylons bring the versatility and power of Ruby on Rails (A popular open-source web framework) to python. It provides an architecture, built around WSGI, that allows the developer to plug in their favorite components.

#### Genshi

- Uses Genshi and Mako which are the two top templating languages in the python web world today. Genshi Is XML based and will serve only valid XML/XHTML files. Using Genshi gains more ability for templates but loses speed.

#### Mako

- Uses Genshi and Mako which are the two top templating languages in the Python web world today. Mako is more similar to HTML. Using Mako loses its ability to use easily working templates, but A major speed boost is gained by using Mako.

### TurboGears Use Cases

#### Full-Stack Web Development

- TurboGears create fully-featured web applications with back-end and front-end integration.

- Build web interfaces for database-driven applications.

#### APIs and Microservices

- Develop RESTful APIs to expose services.

- Integrate microservices into larger systems using its modular design.

#### Data-Intensive Applications

- Handle CRUD operations efficiently with Object-Relational Mapping (ORM).

- Work with SQLAlchemy or MongoDB for data persistence.

#### Prototyping and Rapid Development

- Quickly build prototypes for testing ideas or concepts.

- Use its built-in scaffolding to minimize setup time.

#### Real-Time Web Applications

- Integrate with WebSocket or third-party libraries for real-time functionality.

#### Agile Development

- Fit well with Agile methodologies by enabling fast iterations and flexibility.