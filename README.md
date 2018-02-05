# Hugo-Dashboard

This project is a UI to edit and upload a Hugo repository online. The front end uses React and the back end is a Python Flask API. We are currently testing this over the hugo-academic style but possibly it works for all themes.

## Run API

The API runs on a Python 3 virtual environment (`virtualenv`). Install all dependencies in the `requirements.txt` file and then run the API. These are the steps:

```
cd hugo-dashboard-api
virtualenv -p python3 <env_name>
source <env_name>/bin/activate # on Linux, or source <env_name>/Script/activate in Windows
python src/api.py
```
