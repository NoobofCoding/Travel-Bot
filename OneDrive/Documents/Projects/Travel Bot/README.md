# Travel FAQ Assistant

A simple travel assistant app that answers questions about destinations, visas, weather, and travel tips using AI.

## How It Works

1. You ask a travel question
2. The app compresses your travel guide using Scaledown API
3. Google Gemini AI generates an answer based on the compressed context
4. You get a response about your travel question

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Your API Keys

Edit `.env` file and add:

```
SCALEDOWN_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

### 3. Run the App

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

## Project Structure

```
Travel Bot/
├── .env                      # Your API keys (don't commit this)
├── requirements.txt          # Python packages needed
├── main.py                   # The Streamlit app
├── README.md                 # This file
│
├── data/
│   └── travel_context.txt    # Travel guides and info
│
└── src/
    ├── __init__.py
    ├── scaledown_helper.py   # Handles context compression
    └── llm_helper.py         # Handles AI responses
```

## What You Can Ask

- Do US citizens need a visa for Japan?
- What's the weather like in Thailand in November?
- How much does travel cost in Europe?
- What are the cultural etiquette rules in Thailand?
- Best time to visit Southeast Asia?

## Files

- **scaledown_helper.py** - Sends your travel guide + question to Scaledown API to get relevant context
- **llm_helper.py** - Takes compressed context and asks Gemini AI for an answer
- **travel_context.txt** - Contains your travel information (visas, weather, budgets, etc.)

## Requirements

- Python 3.8+
- Streamlit
- Google Gemini API key
- Scaledown API key

## Notes

- Change the travel context in `data/travel_context.txt` to add more information
- Add more destinations or remove ones you don't need
- The app uses Gemini 2.5 Flash model (fast and cheap)
