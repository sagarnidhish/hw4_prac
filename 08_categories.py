import json
import sqlite3
import openai

# Connect to SQLite database
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Add column if it doesn't exist
#cursor.execute("ALTER TABLE Comments ADD COLUMN Category TEXT")
#conn.commit()

# Fetch comments from the database
cursor.execute("SELECT textOriginal FROM Comments")
rows = cursor.fetchall()

# Load your OpenAI API key
key = "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"
openai.api_key = key    

# Prompt for OpenAI
prompt = """
"Below is a comment from a user on a Youtube video titled 'Sam Altman: OpenAI CEO on GPT-4, ChatGPT, and the Future of AI | Lex Fridman Podcast #367'. Read the comment, analyze it and place it in one of the following categories (explicit explanations are given beside each category title): 
"Technical Discussions": Comments discussing technical aspects, features, or implementation details related to the subject matter of the video.
"Opinions and Feedback": Comments expressing opinions, feedback, or critiques about the content, presentation, or speakers in the video.
"Appreciation and Praise": Comments expressing appreciation, admiration, or praise for the content, speakers, or overall production quality of the video.
"Criticism and Disagreements": Comments containing criticism, disagreements, or counterarguments to the points made in the video or by other commenters.
"Personal Experiences": Comments sharing personal experiences, anecdotes, or stories related to the topic discussed in the video.
"Off-Topic or Irrelevant": Comments that are unrelated to the content of the video or the discussion happening in the comment section.
"Humor and Jokes": Comments containing humor, jokes, or light-hearted remarks related to the content of the video.
"Educational Insights": Comments providing additional insights, explanations, or educational value related to the topic discussed in the video.
"Speculation and Predictions": Comments speculating about future developments, trends, or predictions related to the subject matter of the video.
"Questions and Queries": Comments containing questions, queries, or requests for clarification on certain points discussed in the video. 
"Uncategorized": If the comment does not belong to any one of the ten listed before. 
On the whole, the response should be the category title (written inside " ") only. The comment is:"
"""

# Initialize an empty list to store the responses
category = []

# Process comments one by one
for i, row in enumerate(rows, start=1):
    #if response == "true":  # Check if response is needed
    #print(response)
    textOriginal = row[0]  # Extracting the string from the tuple
    combined_text = prompt + f'"{textOriginal}"'

        # Generate response
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"{combined_text}"}
    #{"role": "sender", "content": "Hi!"}
    ] 
    )   
    data = response.choices[0].message.content.strip()
   
    category.append(data)

    print(f"Category {i} done")
    print(data, type(data))
    print(textOriginal, type(textOriginal))
    #Update SQLite database with the generated reply
    cursor.execute("UPDATE Comments SET Category = ? WHERE textOriginal = ?", (data, textOriginal))
    conn.commit()

# Write data to JSON file
with open('category_outputs.json', 'w') as file:
    json.dump(category, file)

print("Evaluation results saved to category_outputs.json")


# Commit the changes and close the connection
conn.commit()
conn.close()
