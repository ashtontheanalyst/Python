# Flask Login
![Alt Text](./assets/flask.png)  
Simple [login screen](https://www.youtube.com/watch?v=71EU8gnZqZQ) for a flask application: 21:45 (registration logic)

## Virtual Environment for Python Instructions

### Ideas for Later
- The original site from the video had a register and login page, what if I
just wanted a login page and could manually input users into the db. So like
having a user account and an admin account and that's it. Would multiple PCs
be able to log into the same account or will it go boom?
- How do I edit the sqlite DB to either add, remove, or edit users?

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

## Installing SQLite (Linux)
```sh
sudo apt update && sudo apt install sqlite3
```

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