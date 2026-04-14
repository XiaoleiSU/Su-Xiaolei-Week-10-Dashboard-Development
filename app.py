import time

import streamlit as st

from agent import process


def summarize_prompt(prompt: str, max_length: int = 48) -> str:
    cleaned_prompt = " ".join(prompt.split())
    if len(cleaned_prompt) <= max_length:
        return cleaned_prompt
    return f"{cleaned_prompt[:max_length].rstrip()}..."


st.set_page_config(page_title="AI Agent Dashboard", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("AI Agent Dashboard")

with st.sidebar:
    st.header("Configuration")
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
    )

    st.header("History Dashboard")
    clear_history = st.button("Clear History")

    if clear_history:
        st.session_state.history = []
        st.success("History cleared.")

    if st.session_state.history:
        latest_request = st.session_state.history[-1]

        st.subheader("Latest Request")
        st.success("Most recent request")
        st.markdown(f"**Prompt Summary:** {summarize_prompt(latest_request['prompt'])}")
        st.markdown(f"**Temperature:** {latest_request['temperature']:.1f}")
        st.markdown(f"**Elapsed Time:** {latest_request['elapsed_time']:.2f}s")

        st.subheader("Previous Requests")
        previous_requests = list(reversed(st.session_state.history[:-1]))

        if previous_requests:
            for index, item in enumerate(previous_requests, start=1):
                summary = summarize_prompt(item["prompt"])
                with st.expander(f"Request {index}: {summary}"):
                    st.markdown(f"**Prompt:** {item['prompt']}")
                    st.markdown(f"**Response:** {item['response']}")
                    st.markdown(f"**Temperature:** {item['temperature']:.1f}")
                    st.markdown(f"**Elapsed Time:** {item['elapsed_time']:.2f}s")
        else:
            st.caption("No previous requests yet.")
    else:
        st.caption("No requests yet.")

st.markdown("Use this dashboard to send a prompt to a simple AI agent interface.")

left_col, right_col = st.columns([2, 1])

with left_col:
    user_prompt = st.text_area(
        "Enter your prompt",
        placeholder="Type your request here...",
        height=180,
    )
    submitted = st.button("Submit", type="primary")

with right_col:
    st.subheader("Status")
    st.info("Adjust the settings in the sidebar, enter a prompt, and click Submit.")

if submitted:
    if user_prompt.strip():
        try:
            with st.spinner("Processing your request..."):
                start_time = time.perf_counter()
                response = process(user_prompt, temperature)
                elapsed_time = time.perf_counter() - start_time

            st.session_state.history.append(
                {
                    "prompt": user_prompt,
                    "response": response,
                    "temperature": temperature,
                    "elapsed_time": elapsed_time,
                }
            )

            st.success("Prompt submitted successfully.")
            st.subheader("Agent Response")
            st.markdown(
                f"<div style='font-size: 1.15rem; line-height: 1.7;'>{response}</div>",
                unsafe_allow_html=True,
            )

            st.subheader("Request Details")
            details_col1, details_col2 = st.columns(2)
            with details_col1:
                st.metric("Elapsed Time", f"{elapsed_time:.2f}s")
            with details_col2:
                st.metric("Temperature Used", f"{temperature:.1f}")
        except Exception as error:
            st.error(f"Agent error: {error}")
    else:
        st.warning("Please enter a prompt before submitting.")
