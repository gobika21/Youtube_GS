from googleapiclient.discovery import build

def Api_connect():
    api_key = 'AIzaSyCXMb4UYVyVgh0LL7Y_MAOeuyjSbmWqdsQ'
    service_name = 'youtube'
    version = 'v3'

    # Initialize the YouTube API client
    youtube = build(service_name, version, developerKey=api_key)
    return youtube

youtube = Api_connect()