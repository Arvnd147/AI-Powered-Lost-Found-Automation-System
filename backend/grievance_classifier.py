from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
categories = ["Maintenance Issue", "Hostel Problem", "Lost & Found", "Academic Issue", "Other"]

def classify_grievance(description):
    result = classifier(description, categories)
    return result["labels"][0]  # Most probable category