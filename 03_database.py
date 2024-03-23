import json
import sqlite3

# Load JSON data from file
with open('comments.json', 'r') as file:
    data = json.load(file)
    # Add new columns to the table
    
# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS Comments (
                    id TEXT PRIMARY KEY,
                    textDisplay TEXT,
                    textOriginal TEXT,
                    authorDisplayName TEXT,
                    authorChannelUrl TEXT,
                    likeCount INTEGER,
                    viewerRating TEXT,
                    totalReplyCount INTEGER,
                    parentId TEXT,
                    negative INTEGER,
                    angry INTEGER,
                    spam INTEGER,
                    response TEXT
                )''')

# Iterate through JSON data and insert into SQLite table
for comment in data:
    if "topLevelComment" in comment:
        topLevelComment = comment["topLevelComment"]
        snippet = topLevelComment["snippet"]
        id_value = topLevelComment.get("id", None)
        totalReplyCount = comment["totalReplyCount"]
        print("ID:", id_value)  # Debugging print statement
        #print("Total Reply Count:", totalReplyCount)  # Debugging print statement
        cursor.execute('''INSERT OR IGNORE INTO Comments (id, textDisplay, textOriginal, authorDisplayName, authorChannelUrl, likeCount, viewerRating, totalReplyCount, parentId, negative, angry, spam, response)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (id_value,
                        snippet.get("textDisplay", None),
                        snippet.get("textOriginal", None),
                        snippet.get("authorDisplayName", None),
                        snippet.get("authorChannelUrl", None),
                        snippet.get("likeCount", None),
                        snippet.get("viewerRating", None),
                        totalReplyCount,
                        None,  # Parent ID will be NULL for main comments
                        None,  # Initialize negative
                        None,  # Initialize angry
                        None,  # Initialize spam
                        None)) # Initialize response
    else:
        id_value = comment.get("id", None)
        #print("ID:", id_value)  # Debugging print statement
        cursor.execute('''INSERT OR IGNORE INTO Comments (id, textDisplay, textOriginal, authorDisplayName, authorChannelUrl, likeCount, viewerRating, totalReplyCount, parentId, negative, angry, spam, response)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (id_value,
                        comment.get("textDisplay", None),
                        comment.get("textOriginal", None),
                        comment.get("authorDisplayName", None),
                        comment.get("authorChannelUrl", None),
                        comment.get("likeCount", None),
                        comment.get("viewerRating", None),
                        None,
                        comment.get("parentId", None),
                        None,  # Initialize negative
                        None,  # Initialize angry
                        None,  # Initialize spam
                        None)) # Initialize response
                        
# Commit changes and close connection
conn.commit()
conn.close()
