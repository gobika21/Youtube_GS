import mysql.connector

def connect_to_database():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="Youtube"
        )
    cursor = mydb.cursor()
    create_tables(mydb, cursor)

def create_tables(mydb, cursor):
    create_channel_query ='''create table if not exists Channel(
            channel_id varchar(255) PRIMARY KEY,
            channel_name varchar(255),
            channel_description text,
            channel_views int,
            subscription_count int,
            total_video int,
            published_at datetime,
            default_language varchar(255),
            playlist_id varchar(255)
            )'''
    cursor.execute(create_channel_query)
    mydb.commit()

    create_video_content_query='''create table if not exists Video(
            channel_id varchar(255),
            video_id varchar(255) PRIMARY KEY,
            video_name varchar(255),
            video_description text,
            published_at datetime,
            view_count int,
            like_count int,
            comment_count int,
            favorite_count int,
            duration time,
            thumbnail varchar(255),
            caption_status varchar(255)
            )'''
    cursor.execute(create_video_content_query)
    mydb.commit()

    create_comment_query='''create table if not exists Comment(
                comment_id varchar(255) PRIMARY KEY,
                video_id varchar(255),
                comment_text text,
                comment_author varchar(255),
                comment_published_at datetime
            )'''
    cursor.execute(create_comment_query)
    mydb.commit()