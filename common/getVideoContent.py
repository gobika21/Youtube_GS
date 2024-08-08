from common.apiConnect import *
from common.changeDateFormat import change_date_format
from common.changeTimeFormat import change_time_format

# Get videoId's detailed information
def get_video_content(videoId_list):
    videoDetail_list = []
    for vid in videoId_list:
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=vid
        )
        response = request.execute()
    
        for item in response['items']:
            data = dict(
                Channel_Name = item['snippet']['channelTitle'],
                Channel_Id = item['snippet']['channelId'],
                Video_Id = item['id'],
                Video_Name = item['snippet']['title'],
                Video_Description = item['snippet'].get('description'),
                Tags = item.get('tags'),
                Published_At = change_date_format(item['snippet']['publishedAt']),
                View_Count = item['statistics'].get('viewCount'),
                Like_Count = item['statistics'].get('likeCount'),
                Comment_Count = item['statistics'].get('commentCount'),
                Favorite_Count = item['statistics']['favoriteCount'],
                Duration = change_time_format(item['contentDetails']['duration']),
                Thumbnails = item['snippet']['thumbnails']['default']['url'],
                Caption_Status = item['contentDetails']['caption'],
                Definition= item['contentDetails']['definition']
            )
            videoDetail_list.append(data)
    return videoDetail_list 
