import openpyxl
import os
from apiclient.discovery import build
from openpyxl.styles.fills import PatternFill

api_key = 'AIzaSyDDJpQwyJV2AM6y3wfWO14yrVSoyxQf0mU'
path = os.path.abspath('..' + "/samurai_class/template.xlsx")
wb = openpyxl.load_workbook(path)
# print(path)


def get_vedos_search(keyword):
  youtube = build('youtube', 'v3', developerKey = api_key)
  youtube_query = youtube.search().list(q = keyword, part = 'id, snippet', maxResults = 3)
  youtube_res = youtube_query.execute()
  return youtube_res.get('items', [])

result = get_vedos_search('ルフィ')
for i, item in enumerate(result):
  if item['id']['kind'] == 'youtube#video':
    channel_title = item['snippet']['title']
    wb["Sheet1"][f'A{i + 1}'] = channel_title
    print('channel/UC3nxalfo0dZ79qv8zXO6e-A'+item['id']['videoId'])

wb.save("youtube.xlsx")

# def write_to_excel(channel_info): 	# 書き込む


# if __name__ == "__main__":
# 	channel_id_list = ['UCMMjv61LfBy5J3AT8Ua0NGQ', 'UCMMjv61LfBy5J3AT8Ua0NGQ', 'UCMMjv61LfBy5J3AT8Ua0NGQ']
# 	for channel_id in channel_id_list:
# 		channel_info = get_channnel_info()
# 		write_to_excel(channel_info)