import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Download required resources
nltk.download('punk')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Step 1: Read the CSV File
input_csv = "chatbot_data.csv"
df = pd.read_csv(input_csv)


# Step 2-5: Process Questions
def preprocess_question(question):
    tokens = word_tokenize(question.lower())  # Tokenization
    tokens = [word for word in tokens if word not in string.punctuation]  # Remove punctuation
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
    return "-".join(lemmatized_tokens)  # Join with hyphen


df["Processed_Question"] = df["Question"].apply(preprocess_question)

# Step 7: Save Processed Data to CSV
output_csv = "processed_chatbot_data.csv"
df_processed = df[["Processed_Question", "Answer"]]
df_processed.to_csv(output_csv, index=False)

print(f"Processed data saved to {output_csv}")


# Module-2: Chatbot Interaction

def chatbot():
    print("Chatbot is ready! Type 'exit' to stop.")
    df_processed = pd.read_csv(output_csv)

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        processed_input = preprocess_question(user_input)

        response = df_processed[df_processed["Processed_Question"] == processed_input]
        if not response.empty:
            print("Chatbot:", response["Answer"].values[0])
        else:
            print("Chatbot: Sorry, I don't understand.")


# Run chatbot
chatbot()
