import time
import mysql.connector
import streamlit as st

def insert_channel_detail(item):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="Youtube"
    )
    cursor = mydb.cursor()

    # Ensure the unique constraint is in place
    alter_query = '''ALTER TABLE Channel ADD UNIQUE (channel_id)'''
    try:
        cursor.execute(alter_query)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_DUP_KEYNAME:
            # Unique index already exists
            pass
        else:
            st.write(f"Error altering table: {err}")
            mydb.close()
            return

    # Insert query
    insert_channel_query = '''
        INSERT IGNORE INTO Channel (
            channel_id, 
            channel_name, 
            channel_description, 
            channel_views, 
            subscription_count, 
            total_video, 
            published_at, 
            default_language, 
            playlist_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    # Data to be inserted
    data = (
        item['Channel_Id'],
        item['Channel_Name'],
        item['Channel_Description'],
        item['Channel_Views'],
        item['Subscription_Count'],
        item['Total_Video'],
        item['Published_At'],
        item['Default_Language'],
        item['Playlist_Id']
    )

    try:
        cursor.execute(insert_channel_query, data)
        mydb.commit()

        # Check number of affected rows
        if cursor.rowcount > 0:
            msg = st.success("Channel data insert was successful.")
            time.sleep(5)
            msg.empty()
        else:
            msg = st.warning("No rows were affected, channel Id might be a duplicate.")
            time.sleep(5)
            msg.empty()
    except Exception as e:
        mydb.rollback()  # Rollback the transaction if there's an error
        msg = st.error(f"Channel data Insert query failed: {e}")
        time.sleep(5)
        msg.empty()
    finally:
        cursor.close()
        mydb.close()
