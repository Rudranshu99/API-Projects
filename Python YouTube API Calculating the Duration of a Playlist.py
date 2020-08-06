import re
from googleapiclient.discovery import build
#reading API Key from txt file
with open ('API_KEY.txt','r') as f:
    api_key=f.read()

youtube=build('youtube','v3',developerKey=api_key)

nextPageToken=None
hours_pattern=re.compile(r'(\d+)H')
minutes_pattern=re.compile(r'(\d+)M')
seconds_pattern=re.compile(r'(\d+)S')
total_time=0
total_videos=0
while True:
    
    pl_request=youtube.playlistItems().list(
            part='contentDetails',
            playlistId='PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y',
            maxResults=50,
            pageToken=nextPageToken)
    pl_response=pl_request.execute()
    
    vid_ids=[]
    for item in (pl_response['items']):
        vid_ids.append(item['contentDetails']['videoId'])
    
    vid_request= youtube.videos().list(
            part='contentDetails',
            id=','.join(vid_ids))
    
    vid_response=vid_request.execute()
    
    
    
    for item in vid_response['items']:
        duration=item['contentDetails']['duration']
        
        hours=hours_pattern.search(duration)
        minutes=minutes_pattern.search(duration)
        seconds=seconds_pattern.search(duration)
        
        hours=int(hours.group(1)) if hours else 0
        minutes=int(minutes.group(1)) if minutes else 0
        seconds=int(seconds.group(1)) if seconds else 0    
        
        total_time_1=hours*60*60 + minutes*60 + seconds
        print(str((total_time_1//60)//60)+'H '+str((total_time_1//60)%60)+'M '+str(total_time_1%60)+'S')
        print()
        total_time+=total_time_1
        total_videos+=1
        
    nextPageToken=pl_response.get('nextPageToken')
    if not nextPageToken:
        break
print('Total Number of Videos in Playlist='+str(total_videos))
print()
print('Total Time '+str((total_time//60)//60)+'H '+str((total_time//60)%60)+'M '+str(total_time%60)+'S')    

#URL of PLaylist
#https://www.youtube.com/playlist?list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y