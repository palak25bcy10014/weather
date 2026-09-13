# Weather App-Introduction to Programming Project

##  📌Overview
Weather App is a simple Python desktop application that allows
users to search for current weather information by entering a city name.
The application uses Tkinter for the graphical user interface
and Open-Meteo Weather API for weather information.


## 📌Features
* Search weather by city name
* Display temperature
* Display humidity
* Display current weather condition
* Simple graphical user interface
* Error handling for invalid cities


## 📌Technologies/Tools Used
 * Programming Language:  Python 3.7
 * GUI Framework:  Tkinter
 * HTTP Library:  Requests (for API calls)
 * Data Format:  JSON
 * API Service: Open-Meteo Weather API

## 📌Steps to Install & Run the Project
### 1.  *requirement:*
Make sure that Python is installed on your system. You can check this by running the following:
bash
    
     ''' python -->version 3.7 '''
### 2.  *Clone/Download the Repository:*
Download the project files to your local machine.
### 3.  *Install Dependencies:*
This project requires the requests library. In your terminal or command prompt, run the following:
bash
     pip install requests
### 4.  *▶️ Run the Application:*
Go to your project directory and run the script:
 bash
      python Weather.py
    
## 📌Instructions for Testing
Conduct the following tests to ensure that the Weather App works as anticipated.

### 1.  *Standard Weather Search Test:*
* Launch the app
* In the City field, enter "Bhopal"
* Click "Get Weather"

* Expected Output: The application should display the current weather information for Bhopal.

Bhopal

* Temperature: 28°C
* Humidity: 60%
* Weather: Clear

### 2.  *Invalid City Test:*
* Launch the application
* Enter an invalid city name such as "abcdxyz123"

* Click "Get Weather"
* Expected Output: The application should display an error message such as:

City not found or API error

### 3.  *Empty Input Test:*
* Launch the application
* Leave the City field blank
* Click "Get Weather"
* Expected Output: The application should display an error message and should not crash 

Please enter a city name

### 4.  *Offline / Network Error Test:*
* Disconnect your computer from the internet.
* Launch the application.
* Enter a city such as "Mumbai".
* Click "Get Weather".
* Expected Output: The application should remain open and display an error message such as:

City not found or API error

## 📌Project structure
* WeatherApp/
* │
* ├── weather_app.py
* ├── README.md
* ├── statement.md
* ├── screenrecording
* │   └── weather_app.mp4
* └── WeatherApp_Report.pdf
    
## 📌Screenshots
1.Entering the city name

<img width="437" height="407" alt="image" src="https://github.com/user-attachments/assets/12057f25-2cf4-42a3-9898-eea534fa4d34" />


2.weather condition of city

<img width="433" height="412" alt="image" src="https://github.com/user-attachments/assets/fe923409-2678-407d-b762-c511a1940b92" />


3.Error generated when no city is entered and pressed get weather

<img width="431" height="412" alt="image" src="https://github.com/user-attachments/assets/320909ac-144f-40e2-904d-acc92a665d42" />
