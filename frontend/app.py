import streamlit as st


st.title("Web Scraper")


url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)


if st.button("Scrape Website"):

    if url:
        st.success(f"URL entered: {url}")
    else:
        st.warning("Please enter a URL.")