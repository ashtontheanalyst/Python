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

### First start
- The first time you're in the virtual env make sure to run this command so VSCode can register
it later on as a usable python/jupyter kernel
```sh
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
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

## Configuring the Jupyter Environment on VS Code
- Open VSCode and go to your `something.ipynb` file, then enter 'Ctrl + Shift + P'
- Then search 'Python: Select Environment'
- Click 'Enter interpreter path...' and then 'Find...'
- It'll pop up your file system, select the virtual env folder (in this case it's named `/myenv`)
- Navigate to `/Scripts` (on windows) or `/bin` (on Linux) within `/myenv`
- Select the executable python file
- For the **python kernel**, pick the virtual env

## Downloading the 'requirements.txt' File
A `requirements.txt` file contains a list of packages/tools that need to be downloaded in order
to run an application. These are downloaded inside of the virtual environment.
```sh
pip install -r requirements.txt
```