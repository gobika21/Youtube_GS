import time
import mysql.connector
import streamlit as st

def record_exists(cursor, comment_id):
    # Check if the comment already exists in the database
    cursor.execute("SELECT 1 FROM Comment WHERE comment_id = %s", (comment_id,))
    return cursor.fetchone() is not None

def insert_comment_detail(commentDetail_list):
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="A1_youtube"
    )
    cursor = mydb.cursor()

    # SQL INSERT query
    insert_comment_query = '''
        INSERT INTO Comment (
            comment_id,
            video_id,
            comment_text,
            comment_author,
            comment_published_at
        ) VALUES (%s, %s, %s, %s, %s)
    '''

    for comment in commentDetail_list:
        if not record_exists(cursor, comment['Comment_Id']):
            data = (
                comment['Comment_Id'],
                comment['Video_Id'],
                comment['Comment_Text'],
                comment['Comment_Author'],
                comment['Comment_PublishedAt']
            )
            try:
                cursor.execute(insert_comment_query, data)
            except mysql.connector.Error as err:
                msg = st.error(f"Comment Insert query failed for comment_id {comment['Comment_Id']}: {err}")
                time.sleep(5)
                msg.empty()

    mydb.commit()
    msg = st.success("Comment Data insertion process completed.")
    time.sleep(5)
    msg.empty()
    cursor.close()
    mydb.close()