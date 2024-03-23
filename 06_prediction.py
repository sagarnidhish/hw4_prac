import sqlite3
import json
import openai

# Connect to the SQLite database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

cursor.execute("ALTER TABLE Comments ADD COLUMN IF NOT EXISTS Sl_no INTEGER")

# Update Sl_no column using a subquery
cursor.execute("""
    UPDATE Comments 
    SET Sl_no = (
        SELECT COUNT(*) 
        FROM Comments AS t 
        WHERE t.rowid <= Comments.rowid
    )
""")
conn.commit()

# Execute SQL query to retrieve data from a particular column
cursor.execute("SELECT textOriginal FROM Comments")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Close the cursor and connection to the database
cursor.close()
conn.close()

# Load your key into OpenAI
key = "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"
openai.api_key = key

# Load comments from JSON file
#with open('first_1000_comments.json', 'r') as file:
#    comments = json.load(file)

# Prompt for OpenAI
prompt = """
"Below is a comment from a Youtube video. Evaluate it and assign values to these four categories:  'negative', 'angry', 'spam' and 'response' The output of the evaluation should result in a JSON resembling this format: {"negative": 0, "angry": true, "spam": false, "response": true}. 'negative' can take values 0 or 1; the others: 'angry', 'spam' and 'response' each can be assigned true or false (boolean values) individually. To help you do well at this task, here is some additional information: The topic of the Youtube video is: 'Sam Altman: OpenAI CEO on GPT-4, ChatGPT, and the Future of AI | Lex Fridman Podcast #367'. Many comments are nice and congratulatory in sentiment, you can assign 0 for them in the 'negative' category. If they are actually negative according to you, assign them value 1 in the 'negative' category. If the comment has cuss/derogatory words/language and/or the comments are abusive, you can assign 'angry' = true. If the comments seem off topic (like if they are trying to divert attention to something unrelated to the video topic and its likely contents), assign 'spam'=True, else 'spam'=False. Comments with time stamps or some sort of time mentioned is NOT spam. Big comments with specific details are usually NOT spam. If it's a rhetorical question/statement, then 'response' = false. The output should striclty be in the JSON format as described before. Make sure the response format is maintained so that later processing of the responses can be easy and automated. The comment is:"
"""

# Initialize an empty list to store the responses
responses = []

# Process comments one by one
for i, row in enumerate(rows, start=1):
    comment = row[0]
    combined_text = prompt + f'"{comment}"'

    # Generate response
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{combined_text}"}
        #{"role": "sender", "content": "Hi!"}
        ] 
    )

# Extract and store individual response
    #data = response.choices[0].text.strip()
    data = response.choices[0].message.content.strip()
    responses.append(data)

    print(f"Comment {i} done")
    print(data)

# Write data to JSON file
with open('4factors_output.json', 'w') as file:
    json.dump(responses, file)

print("Evaluation results saved to 4factors_output.json")
