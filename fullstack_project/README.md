### For launching the TurboGears Project:
- Create a virtual environment:
    ```bash
    python3 -m venv venv
    . venv/bin/activate
    ```
- Install TurboGears:
    ```bash
    pip install tg.devtools
    ```
- cd into the project:
    ```bash
    cd turbogearsApp
    ```
- Install the project files:
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