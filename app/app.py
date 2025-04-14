import os
from flask import Flask
import psycopg2  # Install with: pip install psycopg2

app = Flask(__name__)

# Database connection details from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

@app.route('/hello')
def hello():
    try:
        # Connect to the database
        connection = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        # Execute the query
        cursor.execute("SELECT current_timestamp;")
        result = cursor.fetchone()
        
        # Close the connection
        cursor.close()
        connection.close()
        
        return f"Current timestamp from database: {result[0]}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)