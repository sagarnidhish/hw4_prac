import json
import sqlite3

conn = sqlite3.connect('comments.db')
c = conn.cursor()

with open('4factors_output.json', 'r') as file:
    data = json.load(file)
    #print(data)
i = 0
for json_string in data:
    # Parse each JSON string into a Python dictionary
    item = json.loads(json_string)
    print(type(item))
    # Extract information from the dictionary
    print("Negative:", item["negative"])
    print("Angry:", item["angry"])
    print("Spam:", item["spam"])
    print("Response:", item["response"])

    # Extract information from the dictionary
    negative = item["negative"]
    angry = "true" if item["angry"] else "false"
    spam = "true" if item["spam"] else "false"
    response = "true" if item["response"] else "false"
    #print(type(negative))
    i = i + 1
    print(i)
    # Update the SQLite database
    c.execute('''UPDATE comments SET negative=?, angry=?, spam=?, response=? WHERE Sl_no=?''', (negative, angry, spam, response, i))
    #c.execute('''UPDATE comments SET negative=?, angry=?, spam=?, response=?''', (negative, angry, spam, response))

# Commit the changes and close the connection
conn.commit()
conn.close()
