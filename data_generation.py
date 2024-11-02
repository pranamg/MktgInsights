from faker import Faker
import random
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

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
    save_to_csv(employees, 'data/employees.csv')
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
    save_to_csv(users, 'data/app_users.csv')
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
    save_to_csv(champions, 'data/champions.csv')
    return champions

def clean_and_preprocess_data(df):
    # Handle missing values
    df = df.dropna()

    # Normalize numerical columns
    scaler = MinMaxScaler()
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df

def aggregate_kpis(users, champions):
    users_df = pd.DataFrame(users)
    champions_df = pd.DataFrame(champions)

    # Aggregate KPIs for app usage
    app_usage_kpis = users_df.groupby('User ID').agg({
        'Number of Visits': 'sum',
        'Duration of Stay': 'mean'
    }).reset_index()

    # Aggregate KPIs for champions by specialization
    champions_kpis = champions_df.groupby('Specialization').agg({
        'Champion ID': 'count'
    }).rename(columns={'Champion ID': 'Number of Champions'}).reset_index()

    save_to_csv(app_usage_kpis, 'data/app_usage_kpis.csv')
    save_to_csv(champions_kpis, 'data/champions_kpis.csv')

    return app_usage_kpis, champions_kpis

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    # Generate the initial employee data
    print("Generating employee data...")
    employees = generate_employees(num_employees=1000)
    print(f"Generated {len(employees)} employees")

    # Generate app users from the employee pool
    print("\nGenerating app users...")
    users = generate_app_users(employees, num_users=200)
    print(f"Generated {len(users)} app users")

    # Generate champions from the users
    print("\nGenerating champions...")
    champions = generate_champions(users, num_champions=20)
    print(f"Generated {len(champions)} champions")

    # Aggregate and save KPIs
    print("\nGenerating KPI reports...")
    app_usage_kpis, champions_kpis = aggregate_kpis(users, champions)
    print("KPI reports generated")

    print("\nAll files have been generated in the 'data' directory:")
    print("- data/employees.csv")
    print("- data/app_users.csv")
    print("- data/champions.csv")
    print("- data/app_usage_kpis.csv")
    print("- data/champions_kpis.csv")
