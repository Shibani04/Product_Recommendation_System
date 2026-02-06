import streamlit as st
import pandas as pd
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Page config
st.set_page_config(
    page_title="Product Recommender Chat",
    page_icon="🛍️",
    layout="centered"
)

# Custom CSS - ChatGPT/Claude style
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: 600;
        text-align: center;
        color: #ffffff;
        margin-bottom: 2rem;
        padding: 1rem;
    }
    
    /* Chat container */
    .stChatMessage {
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
    }
    
    /* User message - right aligned */
    [data-testid="stChatMessageContent"]:has(+ div [data-testid="chatAvatarIcon-user"]) {
        background-color: #f0f0f0;
        border-radius: 18px;
        padding: 0.75rem 1rem;
        margin-left: 20%;
        text-align: left;
    }
    
    /* Assistant message - left aligned */
    [data-testid="stChatMessageContent"]:has(+ div [data-testid="chatAvatarIcon-assistant"]) {
        background-color: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 18px;
        padding: 0.75rem 1rem;
        margin-right: 20%;
    }
    
    /* Hide avatars */
    [data-testid="chatAvatarIcon-user"],
    [data-testid="chatAvatarIcon-assistant"] {
        display: none !important;
    }
    
    /* Sidebar styling - dark background */
    [data-testid="stSidebar"] {
        background-color: #2d2d2d;
    }
    
    /* Sidebar text white */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    /* Sidebar metrics white */
    [data-testid="stSidebar"] [data-testid="stMetricLabel"],
    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        color: white !important;
    }
    
    /* Sidebar button styling */
    [data-testid="stSidebar"] .stButton button {
        background-color: #444444;
        color: white;
        border: 1px solid #555555;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #555555;
        border-color: #666666;
    }
    
    /* Better spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }
    
    /* Input area */
    .stChatInputContainer {
        border-top: 1px solid #e5e5e5;
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.df = None
    st.session_state.client = None

# Load data once (silently)
if st.session_state.df is None:
    try:
        st.session_state.df = pd.read_csv('products_clean.csv')
        st.session_state.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.stop()

# Title
st.markdown('<div class="main-title">Product Recommender Chat</div>', unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What products are you looking for?"):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Search products based on query
    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            
            # Simple keyword search in product names and descriptions
            df = st.session_state.df
            search_terms = prompt.lower().split()
            
            # Filter products containing search terms
            mask = df['product_name'].str.lower().str.contains('|'.join(search_terms), na=False) | \
                   df['about_product'].str.lower().str.contains('|'.join(search_terms), na=False)
            
            results = df[mask].copy()
            
            # Price filter from query
            import re
            price_match = re.search(r'under\s+(\d+)|below\s+(\d+)', prompt.lower())
            if price_match:
                max_price = float(next(g for g in price_match.groups() if g))
                results = results[results['discounted_price'] <= max_price]
            
            # Get top 5 by rating
            results = results.nlargest(5, 'rating')
            
            if len(results) == 0:
                response_text = "Sorry, I couldn't find any products matching your search. Try different keywords!"
            else:
                # Create product list for AI
                product_list = ""
                for idx, row in results.iterrows():
                    product_list += f"\n{row['product_name']}\n"
                    product_list += f"Price: ₹{row['discounted_price']:,.0f}\n"
                    product_list += f"Rating: {row['rating']}/5.0\n"
                    product_list += f"Category: {row['main_category']}\n\n"
                
                # Get AI recommendation
                ai_response = st.session_state.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful shopping assistant. Recommend products based on the user's needs. Be concise and friendly."
                        },
                        {
                            "role": "user",
                            "content": f"User is looking for: {prompt}\n\nAvailable products:\n{product_list}\n\nRecommend the best options and explain why."
                        }
                    ],
                    temperature=0.5,
                    max_tokens=800
                )
                
                response_text = ai_response.choices[0].message.content
            
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})

# Sidebar
with st.sidebar:
    st.header("INFO")
    if st.session_state.df is not None:
        st.metric("Products", len(st.session_state.df))
        st.metric("Categories", st.session_state.df['main_category'].nunique())

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Try asking:")
    st.markdown("""
    - USB cable under 300
    - wireless headphones
    - charging cables
    - gaming mouse
    - phone accessories
    """)
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()