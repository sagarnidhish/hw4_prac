import openai
import json 

# load your key into openai
key = "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"
openai.api_key = key

# call openai - chat completions
response = openai.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
{"role": "user", "content": "How many states are there in the United States of America?"},
#{"role": "sender", "content": "Hi!"}
] 
)
data = response.choices[0].message.content.strip()

# Format the response as a JSON object
response_json = json.dumps({"answer": data})

# Print the JSON object
print(response_json)