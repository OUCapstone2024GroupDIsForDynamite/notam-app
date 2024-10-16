# NOTAM Finder
Our app fetches NOTAM's utilizing the FAA API along a flightpath determined by a user-inputted departure and arrival ICAO or IATA airport codes.

## What NOTAMs Are
NOTAMS are Notifications to the pilots that provide information about flights in the United states, these include important information, like runway closures, airspace restrictions, and malfunctioning equipments. 

## Configuration

To access the FAA API, alter the config.py file in the backend directory to include your client ID and client Secret

## Contribution Guidelines

We use branches per features, which are tickets in our Jira tracker. After completing changes, rebase off of main and sqaush extraneous commits to clean up the commit history. Then, after four approval requests, your branch can be merged to main.

## Setup and Installation Guidelines

### Backend (Flask)
1. Navigate to the `backend` directory.
2. Create a virtual environment and activate it:(Mac)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```

1. Create a virtual environment and activate it:(Windows)

```
python -m venv venv
venv\Scripts\activate
```
If you get an authorization error run: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```

### Frontend (React)
1. Navigate to the `frontend` directory.
2. Install the dependencies:
   ```bash
   npm install
   ```
3. Start the React application:
   ```bash
   npm start
   ```

### Accessing the App
- The React frontend will be available at `http://localhost:3000`.
- The Flask backend API will be available at `http://localhost:5555/api/notams`.
