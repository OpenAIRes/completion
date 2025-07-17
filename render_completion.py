import json
import html

with open('completion.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

model = data.get('model', '')
created = data.get('created')
message = data['choices'][0]['message']['content']
tokens = data['choices'][0].get('logprobs', {}).get('content', [])

rows = []
for entry in tokens:
    token = entry.get('token', '')
    logprob = entry.get('logprob')
    rows.append(f"<tr><td>{html.escape(token)}</td><td>{logprob}</td></tr>")
rows_html = "\n".join(rows)

html_output = f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='utf-8'>
<title>Completion Response</title>
<style>
body {{ font-family: Arial, sans-serif; }}
table {{ border-collapse: collapse; }}
th, td {{ border: 1px solid #999; padding: 4px 8px; }}
</style>
</head>
<body>
<h1>Model: {html.escape(model)}</h1>
<p><strong>Created:</strong> {created}</p>
<p>{html.escape(message)}</p>
<h2>Token Logprobs</h2>
<table>
<tr><th>Token</th><th>Logprob</th></tr>
{rows_html}
</table>
</body>
</html>"""

with open('completion.html', 'w', encoding='utf-8') as f:
    f.write(html_output)
print('Wrote completion.html')
