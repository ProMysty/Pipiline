import psycopg2
from api_requests import mock_data

def connect_to_db():
    print("Connecting to the database.")
    try:
        conn = psycopg2.connect(
            host = "db",
            port = 5432,
            dbname = "weather",
            user = "myst",
            password = "myst"
        )
        print("Connection completed.")
        return conn
    
    except psycopg2.Error as e:
        print(f"Connection failed: {e}")
        raise

def create_table(conn):
    print("Creating the table.")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            name TEXT,
            region TEXT,
            country TEXT,
            timezone_id TEXT,
            local_time TEXT,
            last_updated TEXT,
            is_day DECIMAL,
            temp_celcius FLOAT,
            temp_farenheit FLOAT,
            heatindex_celcius FLOAT,
            heatindex_farenheit FLOAT,
            will_it_rain DECIMAL,
            chance_of_rain DECIMAL
        )
        """)
        conn.commit()
        print("Table creation completed.")
    except psycopg2.Error as e:
        print(f"Creation failed.")
        raise

def insert_records(conn, data):
    print("Inserting records.")
    location = data['location']
    current = data['current']
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO weather_data (
                name,
                region,
                country,
                timezone_id,
                local_time,
                last_updated,
                is_day,
                temp_celcius,
                temp_farenheit,
                heatindex_celcius,
                heatindex_farenheit,
                will_it_rain,
                chance_of_rain
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """, (
            location['name'],
            location['region'],
            location['country'],
            location['tz_id'],
            location['localtime'],
            current['last_updated'],
            current['is_day'],
            current['temp_c'],
            current['temp_f'],
            current['heatindex_c'],
            current['heatindex_f'],
            current['will_it_rain'],
            current['chance_of_rain']
        ))
        conn.commit()
        print("Insertion completed.")
    except psycopg2.Error as e:
        print(f"Insertion failed.")
        raise

def main():
    try:
        conn = connect_to_db()
        data = mock_data()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occured: {e}")
        raise

if __name__ == "__main__":
    main()