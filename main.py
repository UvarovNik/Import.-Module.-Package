
from datetime import datetime, date, time
from Crypto.Cipher import AES
from dirty_main import *


if __name__ == '__main__':
    get_employees()
    calculate_salary()

    print(datetime.today())