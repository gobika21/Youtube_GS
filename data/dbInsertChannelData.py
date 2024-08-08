import mysql.connector
import streamlit as st

def insert_channel_detail(item):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="Youtube"
        )
    cursor = mydb.cursor()

    # alter_query = '''alter table Channel ADD UNIQUE (channel_id)'''

    # cursor.execute(alter_query)

    insert_channel_query = '''
            INSERT INTO Channel (
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

    # cursor.execute(insert_channel_query, data)

    try:
        cursor.execute(insert_channel_query, data)
        mydb.commit()
        
        # Check number of affected rows
        if cursor.rowcount > 0:
            st.write("Channel data insert was successful.")
        else:
            st.write("No rows were affected.")
    except Exception as e:
        mydb.rollback()  # Rollback the transaction if there's an error
        st.write(f"Insert query failed: {e}")