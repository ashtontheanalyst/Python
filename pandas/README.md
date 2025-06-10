# Pandas Tutorial

### Following this video: 
https://www.youtube.com/watch?v=2uvysYbKdjM  
Just wanted to brush up on some skills for data science and work.
<br><br>

## Virtual Environment for Python

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