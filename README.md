# AI Agent Dashboard

## Short System Overview
This project is a Streamlit dashboard for submitting prompts to a simple keyword-based AI agent. The user enters a prompt, adjusts the temperature, and clicks Submit. The app processes the request, shows a response, and stores the interaction in session history.

Key components:
- `app.py`: Dashboard UI, request handling, history, and response display
- `agent.py`: Keyword-based response generator
- `requirements.txt`: Dependencies

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Features Implemented
- Wide-layout dashboard with sidebar configuration
- Temperature slider
- Prompt input and submit button
- Loading spinner, warning, and error messages
- Keyword-based replies for greeting, help, and weather
- Temperature-based response variation
- Request history with highlighted latest request
- Expandable previous requests
- Processing time and temperature details after each request

## Design Decisions
The app was kept simple and lightweight for coursework use. Streamlit was chosen for fast dashboard development, and the agent uses keyword matching instead of a full language model so the behavior stays easy to test and explain.
