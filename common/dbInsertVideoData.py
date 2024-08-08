import mysql.connector
import streamlit as st

def record_exists(cursor, video_id):
    cursor.execute("SELECT 1 FROM Video WHERE video_id = %s", (video_id,))
    # Consume all results to ensure no pending results are left
    return cursor.fetchone() is not None

def insert_video_detail(item):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="Youtube"
    )
    cursor = mydb.cursor()

    # SQL INSERT query
    insert_video_query = '''
        INSERT IGNORE INTO Video (
            channel_id, 
            video_id, 
            video_name, 
            video_description,
            published_at, 
            view_count, 
            like_count, 
            comment_count, 
            favorite_count, 
            duration, 
            thumbnail, 
            caption_status
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    try:
        for video in item:
            if not record_exists(cursor, video['Video_Id']):
                data = (
                    video['Channel_Id'],
                    video['Video_Id'],
                    video['Video_Name'],
                    video['Video_Description'],
                    video['Published_At'],
                    video['View_Count'],
                    video['Like_Count'],
                    video['Comment_Count'],
                    video['Favorite_Count'],
                    video['Duration'],
                    video['Thumbnails'],
                    video['Caption_Status']
                )
                cursor.execute(insert_video_query, data)
        
        mydb.commit()
        st.write("Data insertion process completed.")
    except mysql.connector.Error as err:
        st.write(f"Insert query failed: {err}")
        mydb.rollback()  # Rollback the transaction if there's an error
    finally:
        cursor.close()
        mydb.close()