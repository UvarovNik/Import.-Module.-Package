
from datetime import datetime, date, time
from Crypto.Cipher import AES
from application.modules.salary import calculate_salary
from application.modules.people import get_employees



if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print(datetime.today())