import datetime
from application.salary import calculate_salary
from application.db import people as p


def main():
    print(f'salary: {calculate_salary()}')
    print(f'employees: {p.get_employees()}')
    print(f'today: {datetime.date.today()}')


if __name__ == '__main__':
    main()