# MindMentor

The AI-powered teacher to assist you with your Open Learning problems!

Link to GPT (Requires GPT Plus): https://chat.openai.com/g/g-BLor6Ofy7-mindmentor


# TL;DR

The retrieve_canvas_outcomes.py file uses a GraphQL query to retrieve a list of all the KPIs in the outcomes of the main
OL canvas course.

The retrieve_hboi_framework.py file uses the files in trainingData (retrieved from 
https://github.com/HBO-i/ictresearchmethods.nl/) to condense all of the research methods
from the file tree into one file.

The two files resulting from that are uploaded to a custom GPT from OpenAI,
and with some prompt engineering we create a new GPT that reads both files
and can assist students with the two.


