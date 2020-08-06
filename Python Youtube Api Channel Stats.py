from googleapiclient.discovery import build
with open('API_KEY.txt','r') as f:
	api_key=f.read()
youtube=build('youtube','v3',developerKey=api_key)

#request=youtube.channels().list(part='statistics',forUsername='AddictedA1')
request=youtube.channels().list(part='statistics',id='UCJihyK0A38SZ6SdJirEdIOw')
response=request.execute()
r=response['items'][0]['statistics']
print("Channel Name: Gate Smashers")
print("Total Views ="+r['viewCount'])
print("Subscribers ="+r['subscriberCount'])
print("Total Videos Uploaded="+r['videoCount'])

#https://www.youtube.com/channel/UCJihyK0A38SZ6SdJirEdIOw