import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/scrape"


st.title("Web Scraper")


url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)


if st.button("Scrape Website"):

    if not url:
        st.warning("Please enter a URL.")

    else:
        try:
            response = requests.post(
                API_URL,
                json={
                    "url": url
                }
            )

            if response.status_code == 200:
                data = response.json()

                st.success("Website scraped successfully!")

                st.json(data)

            else:
                st.error(
                    f"Scraping failed: {response.text}"
                )

        except requests.exceptions.RequestException:
            st.error("Could not connect to the FastAPI server.")