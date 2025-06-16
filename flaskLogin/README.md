# Flask Login
![Alt Text](./assets/flask.png)  
Simple [login screen](https://www.youtube.com/watch?v=71EU8gnZqZQ) for a flask application: 14:45min

## Virtual Environment for Python Instructions

### Create the Environment
```sh
python -m venv myenv
```

### Starting it
- Windows:
    ```sh
    myenv\Scripts\activate
    ```
- Linux:
    ```sh
    source myenv/bin/activate
    ```

### Stopping it
- Windows:
    ```sh
    myenv\Scripts\deactivate.bat
    ```
- Linux:
    ```sh
    deactivate
    ```

## Downloading the 'requirements.txt' File
A `requirements.txt` file contains a list of packages/tools that need to be downloaded in order
to run an application. These are downloaded inside of the virtual environment.
```sh
pip install -r requirements.txt
```

## Installing SQLite (Windows)
- Visit [this](https://www.sqlite.org/download.html) page and download a compiled binary
- Extract it into something like `C:\sqlite\`
- **ADD IT AS A ENVIRONMENT VAR.**

## HTML Boiler Plate
- If you open a blank .html file and click "! + Tab", it'll give you this:
```sh
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```