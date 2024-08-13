import streamlit as st
import pandas as pd
import mysql.connector

def showQuestion():
    question = st.selectbox("Select Your Question", (
        "1. What are the names of all the videos and their corresponding channels?",
        "2. Which channels have the most number of videos, and how many videos do they have?",
        "3. What are the top 10 most viewed videos and their respective channels?",
        "4. How many comments were made on each video, and what are their corresponding video names?",
        "5. Which videos have the highest number of likes, and what are their corresponding channel names?",
        "6. What is the total number of likes for each video, and what are their corresponding video names?",
        "7. What is the total number of views for each channel, and what are their corresponding channel names?",
        "8. What are the names of all the channels that have published videos in the year 2022?",
        "9. What is the average duration of all videos in each channel, and what are their corresponding channel names?",
        "10. Which videos have the highest number of comments, and what are their corresponding channel names?"
    ), index=None)

    st.write("You have selected:", question)

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="A1_youtube"
    )
    cursor = db_connection.cursor()

    if question == "1. What are the names of all the videos and their corresponding channels?":
        query1 = """SELECT v.video_name, c.channel_name
                    FROM Video v
                    JOIN Channel c ON v.channel_id = c.channel_id"""
        cursor.execute(query1)
        t1 = cursor.fetchall()
        df1 = pd.DataFrame(t1, columns=["Video Title", "Channel Name"])
        st.write(df1)

    elif question == "2. Which channels have the most number of videos, and how many videos do they have?":
        query2 = """SELECT channel_name AS channelname, total_video AS total_videos 
                    FROM Channel
                    ORDER BY total_videos DESC"""
        cursor.execute(query2)
        t2 = cursor.fetchall()
        df2 = pd.DataFrame(t2, columns=["Channel Name", "No of Videos"])
        st.write(df2)

    elif question == "3. What are the top 10 most viewed videos and their respective channels?":
        query3 = """SELECT v.video_name, c.channel_name, v.view_count
                    FROM Video v
                    JOIN Channel c ON v.channel_id = c.channel_id
                    ORDER BY v.view_count DESC
                    LIMIT 10"""
        cursor.execute(query3)
        t3 = cursor.fetchall()
        df3 = pd.DataFrame(t3, columns=["Video Title", "Channel Name", "Views"])
        st.write(df3)

    elif question == "4. How many comments were made on each video, and what are their corresponding video names?":
        query4 = """SELECT v.video_name, COUNT(cm.comment_id) AS num_comments
                    FROM Video v
                    LEFT JOIN Comment cm ON v.video_id = cm.video_id
                    GROUP BY v.video_name"""
        cursor.execute(query4)
        t4 = cursor.fetchall()
        df4 = pd.DataFrame(t4, columns=["Video Title", "No of Comments"])
        st.write(df4)

    elif question == "5. Which videos have the highest number of likes, and what are their corresponding channel names?":
        query5 = """SELECT v.video_name, c.channel_name, v.like_count
                    FROM Video v
                    JOIN Channel c ON v.channel_id = c.channel_id
                    ORDER BY v.like_count DESC
                    LIMIT 10"""
        cursor.execute(query5)
        t5 = cursor.fetchall()
        df5 = pd.DataFrame(t5, columns=["Video Title", "Channel Name", "Like Count"])
        st.write(df5)

    elif question == "6. What is the total number of likes for each video, and what are their corresponding video names?":
        query6 = """SELECT v.video_name, v.like_count FROM Video v"""
        cursor.execute(query6)
        t6 = cursor.fetchall()
        df6 = pd.DataFrame(t6, columns=["Video Title", "Like Count"])
        st.write(df6)

    elif question == "7. What is the total number of views for each channel, and what are their corresponding channel names?":
        query7 = """SELECT c.channel_name, SUM(v.view_count) AS total_views
                    FROM Channel c
                    JOIN Video v ON c.channel_id = v.channel_id
                    GROUP BY c.channel_name"""
        cursor.execute(query7)
        t7 = cursor.fetchall()
        df7 = pd.DataFrame(t7, columns=["Channel Name", "Total Views"])
        st.write(df7)

    elif question == "8. What are the names of all the channels that have published videos in the year 2022?":
        query8 = """SELECT DISTINCT c.channel_name
                    FROM Channel c
                    JOIN Video v ON c.channel_id = v.channel_id
                    WHERE YEAR(v.published_at) = 2022"""
        cursor.execute(query8)
        t8 = cursor.fetchall()
        df8 = pd.DataFrame(t8, columns=["Channel Name"])
        st.write(df8)

    elif question == "9. What is the average duration of all videos in each channel, and what are their corresponding channel names?":
        query9 = """SELECT c.channel_name, AVG(v.duration) AS avg_duration
                    FROM Channel c
                    JOIN Video v ON c.channel_id = v.channel_id
                    GROUP BY c.channel_name"""
        cursor.execute(query9)
        t9 = cursor.fetchall()
        df9 = pd.DataFrame(t9, columns=["Channel Name", "Average Duration (seconds)"])
        st.write(df9)

    elif question == "10. Which videos have the highest number of comments, and what are their corresponding channel names?":
        query10 = """SELECT v.video_name, c.channel_name, COUNT(cm.comment_id) AS num_comments
                     FROM Video v
                     JOIN Channel c ON v.channel_id = c.channel_id
                     LEFT JOIN Comment cm ON v.video_id = cm.video_id
                     GROUP BY v.video_name, c.channel_name
                     ORDER BY num_comments DESC
                     LIMIT 10"""
        cursor.execute(query10)
        t10 = cursor.fetchall()
        df10 = pd.DataFrame(t10, columns=["Video Title", "Channel Name", "No of Comments"])
        st.write(df10)

    # Close the cursor and the database connection
    cursor.close()
    db_connection.close()