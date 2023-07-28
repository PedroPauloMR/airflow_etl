# Airflow ETL

The ideia is to create a simple dependency in Airflow with some tasks like Bash/Python/Sqlite Operators.

Here, we gonna create some DAGs in order to:
- collect data from a public API (**weatherapi-com.p.rapidapi.com/**)
- save a JSON file named by the day of extraction
- do some transformation bring only few data from this JSON file
- Save as a CSV file