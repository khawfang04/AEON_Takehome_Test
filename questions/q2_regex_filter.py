"""
Task: Extract email components using regex

Write a function that takes a text containing one or more email addresses and returns a list of dictionaries, each with keys:
- "username": part before '@'
- "domain": part after '@'

Example:
  "Please contact support@aeon.co.th or dwh2025@aeonth.com"

Expected Output:
  [
    {"username": "support", "domain": "aeon.co.th"},
    {"username": "dwh2025", "domain": "aeonth.com"}
  ]
"""
import re

def extract_email_user_domain(text:str):
  """
  Extract username and domain for all emails found in the input.
  """
  # username: letters, digits, dot, underscore, percent, plus, hyphen
  # (keeps everything after @)
  pattern = re.compile(r"([A-Za-z0-9._%+\-]+)@([^\s,;:)\]]+)")

  results = []

  for match_name in pattern.finditer(text):
        username, domain = match_name.group(1), match_name.group(2)
        results.append({"username": username, "domain": domain})

  return results

if __name__ == "__main__":
  inputs = ["My Email is Hello-World.123@gmail.com",
    "Please contact support@aeon.co.th or dwh2025@aeonth.com"]

  for text in inputs:
    extracted = extract_email_user_domain(text)
    print(f"Input: {text}")
    print("Extracted:", extracted)
    print()