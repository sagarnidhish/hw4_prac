'''

sqlite3 your_database.db   # Replace `your_database.db` with the path to your SQLite database

.headers on               # Turn on headers to include column names in the CSV
.mode csv                 # Set output mode to CSV
.output your_output_file.csv  # Specify the output file name, e.g., "your_output_file.csv"

SELECT your_column
FROM your_table
LIMIT 25;

.quit                     # Exit SQLite shell

'''
'''
ChatGPT's response to the first 25 comments:

Some prompts to help you classify better: The topic of the Youtube video is:  "Sam Altman: OpenAI CEO on GPT-4, ChatGPT, and the Future of AI | Lex Fridman Podcast #367". Many comments are nice and congratulatory, you can assign 0 for them in the "negative" category. If they are actually negative according to you, assign them value 1 in the "negative" category. The "negative" category can only take values 0 or 1. If they use cuss words and the comments are abusive, you can assign "angry" = true. If the comments seem off topic (like if they are trying to divert attention to something unrelated to this entire topic), assign "spam"=true. If it's a rhetorical question/statement, then "response" = false. If the comment is big and relevant, it would usually require a response. Modify the above responses based on these additional prompts I have given you. 

{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 1, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": true, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}
{"angry": false, "negative": 0, "response": false, "spam": false}




'''