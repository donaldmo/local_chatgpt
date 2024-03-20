import streamlit as st


def clear_input():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""


def set_send_input():
    st.session_state.send_input = True
    clear_input()


def main():
    st.title("Multimodal Local Chat App")
    chat_container = st.container()

    user_input = st.text_input(
        "Type your message here",
        key="user_input",
        on_change=set_send_input
    )

    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            llm_response = "Thi is the response from the LLM model"

            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                st.chat_message("ai").write("here is an answer")

if __name__ == "__main__":
    main()