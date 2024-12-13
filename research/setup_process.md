## Building and Setting Up the Project

### Default boilerplate project:

#### Virtual Environment:
```bash
    sudo apt install python3.10-venv

    python3 -m venv venv

    . venv/bin/activate
```
#### Installation:

- Install TurboGears:
    ```bash
    pip install tg.devtools
    ```
- Create a new project:
    ```bash
    gearbox quickstart app
    cd turboGearsApp
    ```

- Install the project:
    ```bash
    pip install -e . 
    ```
- Downgrade sqlalchemy so that it will serve:
    ```bash
    pip install "sqlalchemy<2.0"
    ```
- Serve the project:
    ```bash
    gearbox serve
    ```

### You can now access the project at http://localhost:8080 and edit the models, comtrollers, and templates to suit your specific needs. 
