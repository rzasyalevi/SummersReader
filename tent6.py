import google.generativeai as genai
import streamlit as st

def setup():
  try:
    gemini_api_key = 'AIzaSyDZz2F4XhXnSSzRwP04grS83eD2Bil6WS4'  # Replace with your actual API key
    genai.configure(api_key=gemini_api_key)
  except Exception as exception:
    raise Exception("An error occurred during setup:", exception)

def summarize_paper(prompt):
  try:
    model = genai.GenerativeModel(model_name='gemini-pro')
    # Enforce prompt for paper summarization
    formatted_prompt = f"Summarize the following paper:\n{prompt}"
    response = model.generate_content(formatted_prompt)
    return response.text
  except Exception as exception:
    raise Exception("An error occurred during text summarization:", exception)

if __name__ == '__main__':
  try:
    setup()
    st.title('Paper Summarizer')
    paper_text = st.text_area("Enter the paper text:")

    if st.button("Summarize"):
      summary = summarize_paper(paper_text)
      st.write("Summary:")
      st.write(summary)
  except Exception as exception:
    print(f"An error occurred: {exception}")
