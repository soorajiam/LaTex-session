## How to get started with running this program

run the command to create a venv in python (assumes python is up and running)
```bash
python3 -m venv .env-name
```

then activate the env using 

```bash
source .env-name/bin/activate
```

create a .env file to store open ai api key

```bash
touch .env

```

add the following to that file

```
OPENAI_API_KEY= YOUR KEY
```

[how to get opn ai api key](https://platform.openai.com/docs/quickstart)

### Then

Change your name in code `main.py` file


then create folder **/job/** 

you can create sub folders in it as much as you like with the job you are applying for.
remember the to create subfolder as the 'job name' which will be asked when running the application

then:

Create 
**/main folder/job/job-you-are-applying-for/job_description.txt**

and copy the job description to that file.

then run
```
python main.py
```

### Warning : open ai usage is sometime costly