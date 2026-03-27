import re

html = input()

title_pattern = r"<title>(.*?)</title>"
body_pattern = r"<body>(.*?)</body>"

title_match = re.search(title_pattern, html)
body_match = re.search(body_pattern, html)

title = title_match.group(1) if title_match else ""
body = body_match.group(1) if body_match else ""

body = re.sub(r"\\n", " ", body)
body = re.sub(r"<.*?>", " ", body)
body = re.sub(r"\s+", " ", body).strip()

print(f"Title: {title}")
print(f"Content: {body}")