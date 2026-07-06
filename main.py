
from datetime import datetime, date, time
from Crypto.Cipher import AES
from application.salary import calculate_salary
from application.db.people import get_employees



if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print(datetime.today())