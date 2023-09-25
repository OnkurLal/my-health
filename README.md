## My Health App

Welcome to My Health! My Health is a comprehensive health management application designed to help you keep track of your medical information and make informed decisions about your health

### Live - https://myhealth.pythonanywhere.com/records/

### How To Use -

- Clone this repo
  - git clone https://gitlab.com/Onkurlal/my-health.git
- Navigate to my-health
  - cd next-weather-app
- Install dependencies
  - pip install -r requirements.txt
- Start development server
  - python manage.py runserver
- This will start the development server at http://localhost:8000. The page will automatically reload if you make changes to the code and save.

### Tech Stack Used

- Python
- HTML
- CSS
- Django
- Calls the [OpenFDA](https://open.fda.gov/apis/) API to get medication information
- Calls the [Natural Library of Medicine Drug Interaction](https://lhncbc.nlm.nih.gov/RxNav/APIs/InteractionAPIs.html#) API to get current drug-drug interactions
