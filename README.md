# Communal Cloud
This project is about building communities that you like! Here, you can register to website, create communities, create roles, workflows, tasks and much more!

Visit our website here: http://communal-cloud.com <br />

Api: http://api.communal-cloud.com <br />

Github: http://git.communal-cloud.com <br />


## Instructions
git clone https://github.com/communal-cloud/communal-cloud.git

### 1. Docker way
cd communal-cloud <br />
docker-compose build <br />
docker-compose up <br />

### 2. Old-school setup
#### 2.1. Backend (Api)
cd communal-cloud/api <br />
pip install -r requirements.txt <br />
python manage.py runserver 0.0.0.0:8000

#### 2.2. Frontend (UI)
cd communal-cloud/ui <br />
npm run serve <br />

Browse http://localhost:8000


## Versions
python: 3.7 <br />
Django>=2.1.7,<2.2.0 <br />
djangorestframework>=3.9.1,<3.10.0 <br />
