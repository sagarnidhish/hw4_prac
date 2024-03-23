import sys
import json
import argparse 

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from YamJam import yamjam       # for managing secret keys
#from datetime import datetime

video_id = 'L_Guz73e6fw'

parser = argparse.ArgumentParser(description='Download comments from youtube')
parser.add_argument('--videoId', type=str, help='url of the video after v=')
args = parser.parse_args()

DEVELOPER_KEY = "AIzaSyBTJbMeUrI56SdPOoujXu642iJwmPaZf1E"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_URL_PREFIX = 'https://www.youtube.com/watch?v='

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

_MAX_RESULTS_PER_QUERY = 100

def get_comment_threads(kwargs):
    comments = youtube.commentThreads().list(
            part='snippet',
            **kwargs,
            ).execute()
    return comments

def parse_item(snippet):
    return snippet

def get_replies(parent_id):
    response = youtube.comments().list(
            part='snippet',
            parentId=parent_id).execute()
    return response['items']

def yield_comments(threads):
    for thread in threads['items']:
        comment_thread = parse_item(thread['snippet'])
        comment_thread['source'] = YOUTUBE_URL_PREFIX + thread['snippet']['videoId']
        yield comment_thread

        if thread['snippet']['totalReplyCount'] != 0:
            for reply in get_replies(thread['id']):
                yield parse_item(reply['snippet'])

def write_comments_to_file(comments, filename):
    with open(filename, 'w') as fp:
        json.dump(comments, fp, indent=2, ensure_ascii=False)

def download_comments(video_id):
    threads = get_comment_threads({
        'videoId': video_id,
        'maxResults': _MAX_RESULTS_PER_QUERY,
    })
    comments = list(yield_comments(threads))

    while 'nextPageToken' in threads:
        threads = get_comment_threads({
            'videoId': video_id,
            'maxResults': _MAX_RESULTS_PER_QUERY,
            'pageToken': threads['nextPageToken']
        })
        comments.extend(yield_comments(threads))

    return comments

if __name__ == "__main__":
    try:
        video_id = args.videoId
    except AttributeError as e:
        sys.stderr.write('Please specify id of the video.\n')
        sys.exit(1)
    
    video_id = 'L_Guz73e6fw'
    comments = download_comments(video_id)
    write_comments_to_file(comments, "comments.json")
    print("Comments have been written to comments.json")
    json.dump(comments, sys.stdout)
