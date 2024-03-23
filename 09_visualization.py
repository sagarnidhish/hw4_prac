import sqlite3
import matplotlib.pyplot as plt

def extract_data_and_count(database_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Execute the query to extract data from the specified columns
    cursor.execute("SELECT negative, angry, spam, Reply FROM Comments")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Initialize counts
    positive_count = 0
    negative_count = 0
    angry_count = 0
    spam_count = 0
    reply_count = 0

    # Extract data and count
    for row in rows:
        negative, angry, spam, reply = row
        if negative == 1:
            negative_count += 1
        else:
            positive_count += 1

        if angry == "true":
            angry_count += 1

        if spam == "true":
            spam_count += 1

        if reply != "None" and reply is not None:
            reply_count += 1

    return {
        #"positive_count": positive_count,
        "negative_count": negative_count,
        "angry_count": angry_count,
        "spam_count": spam_count,
        "reply_count": reply_count
    }


def visualize_counts(counts):
    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Counts')
    plt.title('Counts of Different Comment Categories')

    # Adding data labels
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, 
                 bar.get_height(), 
                 value, 
                 ha='center', 
                 va='bottom')
        
    plt.savefig('visualization.png')
    plt.show()

# Example usage
database_file = "comments.db"
counts = extract_data_and_count(database_file)
print(counts)

# Visualize counts
visualize_counts(counts)



# extracted_data is a list containing many dictionaries

#print((extracted_data[0].get("negative")))
