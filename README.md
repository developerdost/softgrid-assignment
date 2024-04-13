# Softgrid Assignments

1. Create a script that takes in a CSV file as input and outputs a new CSV file that is sorted by the values in the second column, in descending order. The script should also be able to handle and gracefully handle any errors that may occur, such as a missing or improperly formatted CSV file. Additionally, the script should include appropriate comments to explain the logic and any key functions or methods used.

2. Create a web application that allows users to upload, store and retrieve large files (over 2GB) securely. The application should have a user registration and login system, and only registered users should be able to upload and access files. Each file should be encrypted using AES-256 encryption before being stored on the server and should be decrypted when being retrieved. Additionally, the application should have the ability to generate and send secure share links to other users, which allows them to download the files without the need to register or login. The application should also have a built-in feature that automatically deletes files that have been uploaded for over 30 days and send a notification to the uploader. The application should also have a feature that allow user to track their uploads and downloads and show the statistics on the dashboard.


## Installation

Python version >= 3.10.12 required

Create a virtual environment

```bash
python3.10 -m venv venv
````

Activate your virtual environment

```bash
source venv/bin/activate
````

Install the requirement packages

```bash
pip install -r requirements.txt
````

## Task 1
Execute Task 1

```bash
python task_1 file_path_with_name
````

## Task 2 

Install redis-server on ubuntu 22.04

```bash
sudo apt-get install redis-server 
```

Start your development django server

```bash
python manage.py runserver
```

To start the celery beat service:

```bash
celery -A secureuploader.celery beat --loglevel=info 
```

To start the celery worker:

```bash
celery -A secureuploader.celery worker --loglevel=info
```

To open a website:

```
http://127.0.0.1:8000/
```


## Features

- Using AES-256 encryption
- File Download
- File download and upload statics
- Delete 90 days older file
- Send email to user


## Screenshots

![App Screenshot](https://github.com/developerdost/softgrid-assignment/blob/main/screenshots/screenshot_0.png?raw=true)
![App Screenshot](https://github.com/developerdost/softgrid-assignment/blob/main/screenshots/screenshot_1.png?raw=true)
![App Screenshot](https://github.com/developerdost/softgrid-assignment/blob/main/screenshots/screenshot_2.png?raw=true)
![App Screenshot](https://github.com/developerdost/softgrid-assignment/blob/main/screenshots/screenshot_3.png?raw=true)
![App Screenshot](https://github.com/developerdost/softgrid-assignment/blob/main/screenshots/screenshot_4.png?raw=true)
