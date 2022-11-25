# PERFORMANCE TESTING WITH LOCUST

## How to run app
Step 1: `npm i`
Step 2: `npm start`
Step 3: open `localhost:4200` in browser

## How to install
Step 1: Install python
Step 2: `pip install locust`

## How to run locust
### Run with Web-based UI: 
1. Run
- `locust` if you have `locustfile.py`
or
`locust -f src`
or
`locust -f src/file_name.py`

2. Open `localhost:8089` in browser

### Run: Direct command line usage / headless
- `locust --headless --users 10 --spawn-rate 1 -H your_host`


### Install dependencies
##### Install
- `pip install -r requirements.txt`

##### Update install
- `pip install –upgrade -r requirements.txt`

##### Uninstall
- `pip uninstall -r requirements.txt -y`