from common.apiConnect import *

# Get videoId's - playlist
def get_videoId_list(channelId):
    video_ids = []
    response = youtube.channels().list(
        id=channelId,
        part='contentDetails'
    ).execute()

    Playlist_Id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    next_page_token = None

    # maxResults - default = 5, else 0 - 50
    while True:
        playlist_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=Playlist_Id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for i in range(len(playlist_response['items'])):
            video_ids.append(playlist_response['items'][i]['snippet']['resourceId']['videoId'])
        next_page_token = playlist_response.get('nextPageToken')

        if next_page_token is None:
            break
    
    return video_ids