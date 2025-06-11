# Pandas Tutorial

![Alt Text](../assets/panda.gif)

The tutorial by Keith Galli can be found [here](https://www.youtube.com/watch?v=2uvysYbKdjM)

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
<br><br>

## Downloading a 'requirements.txt' File
A `requirements.txt` file contains a list of packages/tools that need to be downloaded in order
to run an application. These are downloaded inside of the virtual environment.
```sh
pip install -r requirements.txt
```