from common.apiConnect import *
from common.changeDateFormat import change_date_format

# Fetch the channel data
def get_channel_data(id):
    response = youtube.channels().list(
        id=id,
        part='snippet,statistics,contentDetails'
    )

    channel_response = response.execute()

    for item in channel_response['items']:
        data = dict(
            Channel_Id=item['id'],
            Channel_Name=item['snippet']['title'],
            Channel_Description=item['snippet']['description'],
            Channel_Views=item['statistics']['viewCount'],
            Published_At = change_date_format(item['snippet']['publishedAt']),
            Subscription_Count=item['statistics']['subscriberCount'],
            Total_Video=item['statistics']['videoCount'],
            Default_Language=item['snippet'].get('defaultLanguage'),
            Playlist_Id=item['contentDetails']['relatedPlaylists']['uploads']
            )
        return data
