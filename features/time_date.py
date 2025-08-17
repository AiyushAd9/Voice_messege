from datetime import datetime

def get_time():
    """Returns the current time in HH:MM AM/PM format"""
    now = datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    """Returns the current date in 'Day, DD Month YYYY' format"""
    now = datetime.now()
    return now.strftime("%A, %d %B %Y")
