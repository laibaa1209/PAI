import re

def date_formatting(text):
    dates_format = r"\b[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}\b"
    date = re.findall(dates_format, text)
    
    return date

text = """
the date blah blah 12/09/2023, blah blah 2023-09-12, and Sep 12,
2023.
"""

dates_found = date_formatting(text)

print("Extracted Date Formats:")
for date in dates_found:
    print(date)
