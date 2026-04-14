# AI Agent Dashboard

## Short System Overview
This project is a simple Streamlit dashboard that demonstrates how a lightweight AI-style agent can process user prompts and return different responses based on keywords. The problem it addresses is building an interactive dashboard interface for submitting text requests, adjusting a temperature setting, and viewing generated responses in a clean layout.

The workflow is straightforward: the user enters a prompt, selects a temperature in the sidebar, and clicks Submit. The app then sends the prompt and temperature to the agent, shows a loading spinner while processing, and displays the response on the page. It also records the request in session history so previous interactions can be reviewed.

The key components are:
- `app.py`: Streamlit user interface, sidebar configuration, request handling, history display, and response details.
- `agent.py`: Keyword-based response generator with template groups for greeting, help, weather, and default responses.
- `requirements.txt`: Project dependency list.

## How to Run the App
1. Open a terminal in the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the local browser link shown in the terminal.

## Features Implemented
- Wide-layout Streamlit dashboard
- Page title: `AI Agent Dashboard`
- Sidebar configuration panel with temperature slider
- Prompt input box and submit button
- Loading spinner during processing
- Warning message for empty input
- Error display for agent failures
- Keyword-based response generation
- Temperature-based response selection behavior
- Request history stored in session state
- Highlighted latest request in the history area
- Expandable previous requests with full response details
- Elapsed processing time and temperature shown after each request
- Larger response text for better readability

## Design Decisions
The dashboard was designed to stay simple, readable, and appropriate for a coursework demonstration. Streamlit was chosen because it supports rapid dashboard development with minimal setup. The agent uses a keyword-matching approach instead of a real LLM so the system remains lightweight, predictable, and easy to explain. Temperature is included to simulate response variability: low temperature gives a stable first response, while higher temperature allows random template selection. Session state is used for history so the interaction flow feels more like a real dashboard without requiring a database.
