import streamlit as st
import os
from openai import OpenAI

# Configure the page
st.set_page_config(page_title="Style-Based Q&A", page_icon="💬")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Sample sentences that define the style
STYLE_EXAMPLES = """
Example 1: This is your first style example sentence.
Example 2: This is your second style example sentence.
Example 3: This is your third style example sentence.
"""

def call_llm(question):
    """
    Call LLM with the question and style examples to generate a styled response
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",  # or your preferred model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions in a specific linguistic style."},
                {"role": "user", "content": f"""
                Here are examples of the linguistic style to use:
                {STYLE_EXAMPLES}
                
                Please answer the following question in the same linguistic style:
                {question}
                """}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Title and description
    st.title("💬 Style-Based Q&A")
    st.write("Ask questions and get answers in a specific linguistic style!")
    
    # Optional: Show style examples
    with st.expander("View Style Examples"):
        st.text(STYLE_EXAMPLES)
    
    # Input field for the question
    question = st.text_area("Enter your question:", height=100)
    
    # Submit button
    if st.button("Get Answer"):
        if question:
            with st.spinner("Generating response..."):
                # Call LLM and get response
                response = call_llm(question)
                
                # Display response in a nice box
                st.info("Response:", icon="🤖")
                st.write(response)
        else:
            st.warning("Please enter a question!")

    # Footer
    st.markdown("---")
    st.markdown("*Powered by OpenAI GPT-4*")

if __name__ == "__main__":
    main()
