import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage, AIMessage

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Convert message history to LangChain message objects
    langchain_messages = []
    for msg in st.session_state['message_history']:
        if msg['role'] == 'user':
            langchain_messages.append(HumanMessage(content=msg['content']))
        elif msg['role'] == 'assistant':
            langchain_messages.append(AIMessage(content=msg['content']))
    
    # Stream the response from the backend with message-level streaming
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response chunks using stream_mode="messages"
        for chunk in chatbot.stream({'messages': langchain_messages}, config=CONFIG, stream_mode="messages"):
            # chunk is a tuple: (message, metadata)
            if len(chunk) >= 1:
                message = chunk[0]
                # Check if it's an AIMessage with content
                if hasattr(message, 'content') and message.content:
                    # Get content directly without stripping to preserve spaces
                    content = str(message.content)
                    
                    # Append the new chunk to build the full response incrementally
                    if hasattr(message, 'response_metadata') or type(message).__name__ == 'AIMessageChunk':
                        # This is a streaming chunk, append it
                        full_response += content
                    else:
                        # This is the complete message
                        full_response = content
                    
                    # Update the placeholder with markdown for better readability
                    message_placeholder.markdown(full_response)
        
        # Final response with markdown formatting
        message_placeholder.markdown(full_response)
    
    # Add the complete assistant response to message_history
    st.session_state['message_history'].append({'role': 'assistant', 'content': full_response})