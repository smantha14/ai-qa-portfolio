import anthropic

client = anthropic.Anthropic()   # reads API key from environment
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[{"role": "user", "content": "Say hello politely."}],
)
print(response.content[0].text)