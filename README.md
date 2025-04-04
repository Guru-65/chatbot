Overview
This project is a simple AI chatbot developed using Python, pandas, and Natural Language Processing (NLP) techniques. The chatbot processes a CSV file containing questions and answers, prepares the data for effective matching, and allows user interaction to retrieve appropriate responses.

Features
Data preprocessing: Tokenization, stopword removal, and lemmatization

CSV handling for question-answer mapping

Simple text-based chatbot interface

Technologies Used
Python

pandas

NLTK (Natural Language Toolkit)

Prerequisites
Make sure you have the following installed:

Python (3.x)

pandas

nltk

You can install the required Python packages using:

bash
Copy
pip install pandas nltk
Files
chatbot_data.csv: Input CSV file containing questions and answers.

processed_chatbot_data.csv: Output CSV file with processed questions and corresponding answers.

chatbot.py: The main script that processes the data and runs the chatbot.

How It Works
Module 1: Data Preparation and Processing
Read CSV File: Loads the input file chatbot_data.csv.

Preprocess Questions:

Tokenization

Removal of stopwords and punctuation

Lemmatization

Joining tokens with hyphens

Save Processed Data: Outputs the processed questions and answers into processed_chatbot_data.csv.

Module 2: Chatbot Interaction
Prompts the user for input

Processes the input similarly to the training data

Matches the preprocessed user input with the processed questions

Displays the corresponding answer or a default "I don’t understand" message

How to Run
Ensure chatbot_data.csv is in the same directory as the script.

Run the script:

bash
Copy
python chatbot.py
Start chatting! Type your question and press Enter.

Type exit to end the chat session.

Example Input & Output
vbnet
Copy
You: What is your name?  
Chatbot: Sorry, I don't understand.  

You: Tell me about the weather.  
Chatbot: It's sunny and warm today.  

You: exit  
Notes
The chatbot matches exact processed questions, so variations in phrasing may not work unless preprocessed similarly.

Ensure the input CSV file is formatted correctly with Question and Answer columns.

Troubleshooting
Error: ModuleNotFoundError for nltk or pandas

Install using pip install nltk pandas

No response for valid questions

Check if the question matches the format of questions in the CSV file.
