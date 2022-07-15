from flask import Flask, render_template
from datetime import date, datetime,  timezone
from zoneinfo import ZoneInfo


#Get Current Date
def get_current_date():
    now = datetime.now()
    return now

#Format Current Date
def format_current_date():
    date_today = get_current_date().strftime("%A | %B %d, %Y")
    return date_today

#Format Current Time
def current_time():
    current_time = get_current_date().strftime("%H:%M %p")
    return current_time

#Calculate number of days to New Year 2023
def days_to_ny():
    today_in_number = int(get_current_date().strftime("%j"))
    ny_date = datetime.strptime("12-31-2022", '%m-%d-%Y')
    # display_ny_date = ny_date.strftime("%a | %B %d")
    ny_in_number = int(ny_date.strftime("%j"))
    ny_days = ny_in_number - today_in_number
    return ny_days

#Calculate number of hours to New Year 2023
def hours_to_ny():
    hours = days_to_ny() * 24
    return hours

#Calculate number of minutes to New Year 2023
def mins_to_ny():
    minutes =  days_to_ny() * 1440
    return minutes



app = Flask(__name__)


@app.route('/')

def home():
    return render_template("home.html", current_date=format_current_date(), 
    time_now=current_time(), days=days_to_ny(), hours=hours_to_ny(), minutes=mins_to_ny())
    

@app.route('/about/')

def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)



