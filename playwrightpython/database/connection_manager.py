import psycopg2
from psycopg2.extras import RealDictCursor

from playwrightpython.utils.database_credential import DBDetails, DBCredDetails


def fetch_data_from_postgres(query):
    """
    Connect to PostgreSQL, execute the query, and fetch results as a list of dictionaries.

    :param query: SQL query to execute
    :param db_config: Dictionary containing database connection details
    :return: List of dictionaries with column names as keys and column values as values
    """
    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname=DBDetails.DBNAME.db_value,
            user=DBCredDetails.USER.db_cred_value,
            password=DBCredDetails.PASSWORD.db_cred_value,
            host=DBDetails.HOST.db_value,
            port=DBDetails.PORT.db_value
        )

        # Create a RealDictCursor object
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        # Execute the query
        cursor.execute(query)

        # Fetch all results as a list of dictionaries
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return results
    except Exception as e:
        print(f"Error while fetching data from PostgreSQL: {e}")
        return []
