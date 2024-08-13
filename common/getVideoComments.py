from common.apiConnect import *
from common.changeDateFormat import change_date_format

# Get each video's comments
def get_video_comments(videoId_list):
    commentDetail_list = []
    try:
        for vid in videoId_list:
            request = youtube.commentThreads().list(
                part='snippet',
                videoId=vid,
                maxResults=50 # 100 comments
            )
            response = request.execute()

            for item in response['items']:
                data = dict(
                    Video_Id = item['snippet']['topLevelComment']['snippet']['videoId'],
                    Comment_Id = item['snippet']['topLevelComment']['id'],
                    Comment_Text = item['snippet']['topLevelComment']['snippet']['textDisplay'],
                    Comment_Author = item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                    Comment_PublishedAt = change_date_format(item['snippet']['topLevelComment']['snippet']['publishedAt'])
                )
                commentDetail_list.append(data)
    except:
        pass
    return commentDetail_list