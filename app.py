import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# CSS inject karna
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Skills", "Contact"])

# Function to load HTML file
def load_html(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

# Display selected page
if page == "Home":
    st.components.v1.html(load_html("index.html"), height=800, scrolling=True)

elif page == "About":
    st.components.v1.html(load_html("about.html"), height=800, scrolling=True)

elif page == "Projects":
    st.components.v1.html(load_html("projects.html"), height=800, scrolling=True)

elif page == "Skills":
    st.components.v1.html(load_html("skills.html"), height=800, scrolling=True)

elif page == "Contact":
    st.components.v1.html(load_html("contact.html"), height=800, scrolling=True)
