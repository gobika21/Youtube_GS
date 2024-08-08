import streamlit as st
import pandas as pd
import math
from pathlib import Path
from common.dbCreateTable import *
from common.dbInsertChannelData import insert_channel_detail
from common.dbInsertCommentData import insert_comment_detail
from common.dbInsertVideoData import insert_video_detail
from common.getChannelData import get_channel_data
from common.getVideoComments import get_video_comments
from common.getVideoContent import get_video_content
from common.getVideoIdList import get_videoId_list

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Youtube dashboard',# This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def main():
    """Youtube Harveseting dashboard

    Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.
    """


main_df = main()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# Youtube Harveseting dashboard

Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.

'''
# Connect with youtube service
channelId = st.text_input("Youtube Channel ID", "UCwF9iGns10no6ZmZUtEce6g")
st.write("The current youtube channel id is", channelId)

def getYoutubeDetails(channelId):
    channelData = get_channel_data(channelId)
    insert_channel_detail(channelData)

    # st.write("Channel Name:", channelData['Channel_Name'])
    # st.write("Channel Description:", channelData['Channel_Description'])
    # st.write("Total Video:", channelData['Total_Video'])
    # st.write("Subscription Count:", channelData['Subscription_Count'])
    # st.write("Channel Views:", channelData['Channel_Views'])
    # st.write("Published At:", channelData['Published_At'])

    videoIds = get_videoId_list(channelId)
    videoContent = get_video_content(videoIds)
    # st.write("video content", videoContent)
    insert_video_detail(videoContent)

    videoComments = get_video_comments(videoIds)

    insert_comment_detail(videoComments)

    # return channelData, videoContent, videoComments

    connect_to_database()
    
    # st.write("video Details", videoContent)
    # st.write('video comments', videoComments)

getYoutubeDetails(channelId)

