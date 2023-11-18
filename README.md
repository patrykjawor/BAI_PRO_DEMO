# BAI_PRO_DEMO
BAI project shows common vulnerabilities in web applications as well as ways to mitigate the risk.


## Installation
```sh
git clone https://orkan.tu.kielce.pl/gitlab/Kuba.J/bai_pro_demo.git
cd bai_pro_demo
cd backend
conda create --name <env> --file requirements.txt
python manage.py migrate
python manage.py makemigrations mainApp
python manage.py migrate
python manage.py makemigrations django_otp
python manage.py migrate
cp backend/env.schema backend/.env
cd ../frontend
npm i
```
To set up environment properly please define `EMAIL_HOST` `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` variables in `.env` file.

## Usage
To start server use this commands:

```sh
cd backend
conda activate <env>
python manage.py runserver
```

To start Node.js developer server use this command:
```sh
cd frontend
npm run dev
```

## Authors
<h3>Jakub Jach<br/>
Patryk Jaworski
</h3>
