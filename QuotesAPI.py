# Function to fetch a random quote from the ZenQuotes API
def fetch_random_quote():
    import requests
    try:
        # ZenQuotes API endpoint
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            return f'"{quote}"\n\n- {author}'
        else:
            return "Failed to fetch quote. Please try again later."
    except Exception as e:
        return f"Error: {e}"