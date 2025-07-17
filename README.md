# Completion JSON Sample

This repository contains a sample response from the OpenAI Chat Completion API.
The file `completion.json` is the unmodified JSON that was returned by GPT-4
when asked a simple question. Use `render_completion.py` to generate a
`completion.html` file with a formatted view of this data.

## Source of the JSON

The `completion.json` file was produced by sending a request to the
`/v1/chat/completions` endpoint. A single user message was provided and the
response includes log probability information for each generated token.
Key request parameters were:

- **model**: `gpt-4.1-2025-04-14`
- **temperature**: `1.0`
- **top_p**: `1.0`
- **logprobs**: `true`

The following Python snippet demonstrates a similar request using the OpenAI
Python library:

```python
import openai

response = openai.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=[{"role": "user", "content": "Hello"}],
    temperature=1.0,
    top_p=1.0,
    logprobs=True,
)
```

`completion.json` stores the raw JSON of that response for reference.

## Usage

You can inspect the file with `jq` to explore the response structure:

```bash
jq '.' completion.json
```

The assistant's reply is available at `choices[0].message.content` and reads:

```
Hi! How can I help you today?
```

This repository is primarily a simple example of what a Chat Completion API
response looks like and how you might parse it in scripts or other tools.

### Render HTML

The repository now includes `render_completion.py`, a small script that reads
`completion.json` and generates an HTML view. Running the script will create or
overwrite `completion.html` with a table of each token and its log probability:

```bash
python3 render_completion.py
```

Open `completion.html` in your browser to see the formatted output.

