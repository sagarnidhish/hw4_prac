import sqlite3
import json

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Step 2: Query the database to retrieve the data
cursor.execute("SELECT * FROM Comments")
data = cursor.fetchall()

# Step 3: Convert the data into a suitable JSON format
# Assuming the structure of the comments table: (id, user_id, comment_text, timestamp)
# You might need to adjust this based on your actual table structure
clean_data = []
for row in data:
    id_value, textDisplay, textOriginal, authorDisplayName, authorChannelUrl, likeCount, viewerRating, totalReplyCount, parentId, negative, angry, spam, response, Sl_no, Reply, Category = row
    comment_entry = {
        "Sl_no": Sl_no,
        "id": id_value,
        "textDisplay": textDisplay,
        "textOriginal": textOriginal,
        "authorDisplayName": authorDisplayName,
        "authorChannelUrl": authorChannelUrl,
        "likeCount": likeCount,
        "viewerRating": viewerRating,
        "totalReplyCount": totalReplyCount,
        "parentId": parentId,
        "negative": negative,
        "angry": angry,
        "spam": spam,
        "response": response,
        "Reply": Reply,
        "Category": Category          
    }
    clean_data.append(comment_entry)

# Step 4: Write the JSON data to the "clean_dataset.json" file
with open('clean_dataset.json', 'w') as json_file:
    json.dump(clean_data, json_file, indent=4)

# Close the database connection
conn.close()
