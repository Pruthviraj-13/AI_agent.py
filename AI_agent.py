import streamlit as st


TOPIC_RESPONSES = {
    "machine learning": (
        "Machine learning is a branch of AI where computers learn patterns "
        "from data and use those patterns to make predictions or decisions."
    ),
    "python": (
        "Python is a beginner-friendly programming language widely used for "
        "web apps, automation, data science, and AI."
    ),
    "ai": (
        "Artificial intelligence is the field of building systems that can "
        "perform tasks that usually need human intelligence, such as reasoning, "
        "learning, and understanding language."
    ),
    "data science": (
        "Data science combines statistics, programming, and domain knowledge "
        "to turn data into useful insights."
    ),
}

SAMPLE_QUESTIONS = [
    "What is AI?",
    "Explain machine learning",
    "Why is Python used in data science?",
    "What is data science?",
]


def get_response(question: str) -> str:
    """Return a study-friendly response for the user's question."""
    normalized_question = question.strip().lower()

    for keyword, response in TOPIC_RESPONSES.items():
        if keyword in normalized_question:
            return response

    return (
        "I am still learning that topic. Try asking about AI, machine learning, "
        "Python, or data science."
    )


def main() -> None:
    st.set_page_config(page_title="AI StudyBuddy", page_icon=":books:")

    st.title("AI StudyBuddy")
    st.write("Ask me simple educational questions and I will explain them clearly.")

    with st.sidebar:
        st.header("Try asking")
        for question in SAMPLE_QUESTIONS:
            st.caption(question)

    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Enter your question:")

    if st.button("Ask", type="primary") and user_input.strip():
        response = get_response(user_input)
        st.session_state.history.append((user_input.strip(), response))

    if st.session_state.history:
        st.subheader("Answer")
        latest_question, latest_response = st.session_state.history[-1]
        st.info(latest_question)
        st.success(latest_response)

        with st.expander("Question history"):
            for question, answer in reversed(st.session_state.history):
                st.markdown(f"**Q:** {question}")
                st.markdown(f"**A:** {answer}")


if __name__ == "__main__":
    main()
