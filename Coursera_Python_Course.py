"""BLAHBLAHBLAH"""
import datetime as dt
date = dt.date
datetime = dt.datetime

def days_in_month(year, month):
    """BLAHBLAHBLAH"""
    if month == 12:
        return 31
    return (date(year, month+1, 1) - date(year, month, 1)).days

def is_valid_date(year, month, day):
    """BLAHBLAHBLAH"""
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def days_between(y_1, m_1, d_1, y_2, m_2, d_2):
    """BLAHBLAHBLAH"""
    if not is_valid_date(y_1, m_1, d_1) or not is_valid_date(y_2, m_2, d_2):
        return 0
    
    days = (date(y_2, m_2, d_2) - date(y_1, m_1, d_1)).days
    if days < 0:
        return 0
    else:
        return days

def age_in_days(year, month, day):
    """BLAHBLAHBLAH"""
    if not is_valid_date(year, month, day):
        return 0
    
    today = datetime.today().date()
    birthday = date(year, month, day)
    if birthday > today:
        return 0
    
    return (today - birthday).days