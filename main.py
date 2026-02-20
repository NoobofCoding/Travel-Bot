import streamlit as st
from src.scaledown_helper import compress_travel_context
from src.llm_helper import get_ai_response

# 1. Page Configuration
st.set_page_config(page_title="Travel FAQ Assistant", page_icon="✈️")
st.title("✈️ Travel FAQ Assistant")
st.write("Ask me anything about your travel destination, visas, or weather!")

# 2. Initialize Chat History in Streamlit Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle User Input
user_input = st.chat_input("E.g., Do US citizens need a visa for Japan?")

if user_input:
    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process the response with a loading spinner
    with st.chat_message("assistant"):
        with st.spinner("Compressing context and generating answer..."):
            try:
                # Step A: Compress the massive travel context + user query
                compressed_data = compress_travel_context(user_input)
                
                # Step B: Get the final answer from Gemini
                final_answer = get_ai_response(compressed_data)
                
                # Step C: Display it
                st.markdown(final_answer)
                st.session_state.messages.append({"role": "assistant", "content": final_answer})
            
            except Exception as e:
                st.error(f"An error occurred: {e}")
