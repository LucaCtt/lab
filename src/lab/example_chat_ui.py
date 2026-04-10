import json
import streamlit as st
import litellm
from litellm.utils import function_to_dict

from lab.settings import Settings
from lab.tools import functions

settings = Settings()
if not settings.litellm_api_key:
    st.error("Set LITELLM_API_KEY to your LiteLLM master key or user key.")
    st.stop()

litellm.api_base = settings.litellm_base_url
litellm.api_key = settings.litellm_api_key


def _completion_kwargs():
    return {
        "model": settings.model,
        "max_tokens": settings.max_tokens,
        "temperature": settings.temperature,
        "top_p": settings.top_p,
        "top_k": settings.top_k,
        "presence_penalty": settings.presence_penalty,
        "repetition_penalty": settings.repetition_penalty,
        "extra_body": {"chat_template_kwargs": {"enable_thinking": False}},
    }


tools = [
    {"type": "function", "function": function_to_dict(f)} for f in functions.values()
]

st.title("Chat")

if "messages" not in st.session_state:
    messages: list[litellm.Message | dict] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    st.session_state.messages = messages

# Display chat history (skipping tool/system messages for UI cleanliness)
for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"] and message.get("content"):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask anything"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        # 1. Initial Call to check for Tool Calls (Stream must be False for tools)
        response = litellm.completion(
            **_completion_kwargs(),
            messages=st.session_state.messages,
            tools=tools,
            stream=False,
        )
        if not isinstance(response, litellm.ModelResponse):
            st.error(
                "Tool calls are not supported in streaming mode. Please disable streaming."
            )
            st.stop()

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls or []

        # Handle tool execution if the model requested it
        if tool_calls:
            # Append the assistant's tool call request to history
            st.session_state.messages.append(response_message.to_dict())

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if not function_name or function_name not in functions:
                    continue

                with st.expander(f"🛠️ Tool Call: {function_name}", expanded=False):
                    st.write("**Parameters:**")
                    st.code(json.dumps(function_args, indent=2), language="json")

                    try:
                        result = str(functions[function_name](**function_args))
                    except Exception as e:
                        result = f"Error: {str(e)}"

                    st.write("**Output:**")
                    st.info(result)

            # 2. Final Call to summarize results (Streaming allowed here)
            response = litellm.completion(
                **_completion_kwargs(), messages=st.session_state.messages, stream=True
            )

        # Handle Final Text Output (Streamed or Static)
        response_placeholder = st.empty()  # Reset placeholder for final response
        full_response = ""
        if isinstance(response, litellm.ModelResponse):
            full_response = response.choices[0].message.content or ""
            response_placeholder.markdown(full_response)
        else:
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                response_placeholder.markdown(full_response + "▌")
            response_placeholder.markdown(full_response)

        # Store the final text response
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
