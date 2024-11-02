from faker import Faker
import random

fake = Faker()

def generate_employees(num_employees=1000):
    employees = []
    for _ in range(num_employees):
        employee = {
            "Employee ID": fake.uuid4(),
            "Name": fake.name(),
            "Rank": random.choice(["Junior", "Mid", "Senior", "Lead"]),
            "Role": random.choice(["Engineer", "Manager", "Analyst", "Designer"]),
            "Location": fake.city(),
            "Age": random.randint(22, 65),
            "Gender": random.choice(["Male", "Female", "Non-binary"])
        }
        employees.append(employee)
    return employees

def generate_app_users(employees, num_users=200):
    users = []
    employee_subset = random.sample(employees, num_users)
    for employee in employee_subset:
        user = {
            "User ID": employee["Employee ID"],
            "Name": employee["Name"],
            "Age": employee["Age"],
            "Gender": employee["Gender"],
            "Number of Visits": random.randint(1, 100),
            "Duration of Stay": random.uniform(1, 10),
            "Features Used": random.sample(["Feature A", "Feature B", "Feature C", "Feature D"], random.randint(1, 4))
        }
        users.append(user)
    return users

def generate_champions(users, num_champions=20):
    champions = []
    user_subset = random.sample(users, num_champions)
    for user in user_subset:
        champion = {
            "Champion ID": user["User ID"],
            "Name": user["Name"],
            "Age": user["Age"],
            "Gender": user["Gender"],
            "Specialization": random.choice(["Specialization A", "Specialization B", "Specialization C"])
        }
        champions.append(champion)
    return champions
