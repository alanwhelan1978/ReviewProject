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
    while True:
        print("Please enter a review for Service, Food, Cleanliness and Staff")
        print("Scores should be between 1 and 5.")
        print("The four numbers need to be seperated by a comma")
        print("5 being the best and 1 being the worse")
        print("Example: 5,4,4,5\n")

        data_str = input("Enter your data here: \n")

        review_data = data_str.split(",")

        if validate_data(review_data):
            print("Data is valid!")
            break

    return review_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into
    integers or if there aren't exactly 4 values. Also
    stops user adding integers higher than 5
    """
    try:
        a = [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"Exactly 4 values required, you provided {len(values)}"
            )
        for value in a:
            if value not in list(range(1, 6)):
                raise ValueError("Score needs to be between 1 and 5\n")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

        return False
    return True


def update_review_worksheet(data):
    """
    update review worksheet, add a new row with the data input
    """
    print("Adding your review......\n")
    review_worksheet = SHEET.worksheet("review")
    review_worksheet.append_row(data)
    print("Review added sucessfully.\n")

data = get_review_data()
review_data = [int(num) for num in data]
update_review_worksheet(review_data)
