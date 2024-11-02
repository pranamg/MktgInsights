# Marketing Insights

## Project Description

Marketing Insights is a data-driven project aimed at generating and analyzing employee data, app user data, and champion data. The project uses the Faker library to generate synthetic data and pandas for data manipulation and analysis. The generated data is saved in CSV files and can be used for various marketing insights and strategies.

## Documentation

### Dependencies

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

### Data Generation

The `data_generation.py` script generates the following data:

- Employee data
- App user data
- Champion data
- App usage KPIs
- Champions KPIs

To generate the data, run the following command:

```
python data_generation.py
```

The generated files will be saved in the `data` directory:

- `data/employees.csv`
- `data/app_users.csv`
- `data/champions.csv`
- `data/app_usage_kpis.csv`
- `data/champions_kpis.csv`

### Streamlit App

The project includes a Streamlit app for visualizing the generated data. To run the Streamlit app, use the following command:

```
streamlit run streamlit_app.py
```

The app now imports data directly from the CSV files in the `data` directory using `pd.read_csv`. The app provides a dashboard with key metrics and visualizations for employees, app usage, and champions.

## Further Reading

- [Faker Documentation](https://faker.readthedocs.io/en/master/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Streamlit Documentation](https://docs.streamlit.io/)
