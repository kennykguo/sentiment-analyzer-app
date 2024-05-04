#Import libraries
import spacy
import pathlib

#load spacy's default language
nlp = spacy.load("en_core_web_sm")

# Construct a doc object, which a sequence of token objects, representing a lexical token
# Each token has information about a particular piece of text
# print(nlp)

# Create a Doc object, which allows us to access information about the processed text
introduction_doc = nlp("This tutorial is about Natural Language Processing in spaCy. ")

# print(type(introduction_doc))

# The doc is separated into tokens, which breaks down the sentence into its individual words
# Create a series of Token objects
# print([token.text for token in introduction_doc])

file_name = "introduction.txt"

introduction_doc = nlp(pathlib.Path(file_name).read_text(encoding="utf-8"))
print ([token.text for token in introduction_doc])