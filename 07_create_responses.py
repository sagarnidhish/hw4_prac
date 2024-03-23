import json
import sqlite3
import openai

# Connect to SQLite database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Add column if it doesn't exist
try:
    cursor.execute("ALTER TABLE Comments ADD COLUMN Reply TEXT")
except sqlite3.OperationalError as e:
    print("Column already exists:", e)
#cursor.execute("ALTER TABLE Comments ADD COLUMN IF NOT EXISTS Reply TEXT")
conn.commit()

# Fetch comments from the database
cursor.execute("SELECT textOriginal, response FROM Comments")
rows = cursor.fetchall()

# Load your OpenAI API key
key = "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"
openai.api_key = key    

# Prompt for OpenAI
prompt = """
"Below is a question/comment from a user on a Youtube video titled 'Sam Altman: OpenAI CEO on GPT-4, ChatGPT, and the Future of AI | Lex Fridman Podcast #367'. Only if it is a question, or if the user is explicitly asking for an answer/reply, please generate an appropriate reply. The reply should be well-mannered and brief. It should make the reader feel like as if Lex Freidman himself has replied. It should sound humanly, not robotic. It should respect the sentiments of the person who has commented. If you think the comment does not need a reply, just reply "None". If you are giving a reply, the response should NOT be in this format "Reply: ...". The comment is: "
"""

# Initialize an empty list to store the responses
reply = []

# Process comments one by one
for i, (textOriginal, response) in enumerate(rows, start=1):
    if response == "true":  # Check if response is needed
        print(response)
        combined_text = prompt + f'"{textOriginal}"'

        # Generate response
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{combined_text}"}
        #{"role": "sender", "content": "Hi!"}
        ] 
        )   
        # Extract and store individual response
        data = response.choices[0].message.content.strip()
    else:
        data = None  # If reply is not needed, set data to None

    reply.append(data)

    print(f"Reply {i} done")
    print(data)

    # Update SQLite database with the generated reply
    cursor.execute("UPDATE Comments SET Reply = ? WHERE textOriginal = ?", (data, textOriginal))
    conn.commit()

# Write data to JSON file
with open('reply_outputs.json', 'w') as file:
    json.dump(reply, file)

print("Evaluation results saved to reply_outputs.json")

# Commit the changes and close the connection
conn.commit()
conn.close()
