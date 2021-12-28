import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('review_sheet')


def get_review_data():
    """
    Get review score input from user
    """
    print("Please enter your review scores for Service Food Cleanliness and Staff")
    print("Scores should be between 1 and 5. 5 being the best and 1 being the worse")
    print("Example: 5,4,4,5,3\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_review_data()  


