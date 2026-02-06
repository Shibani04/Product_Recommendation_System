# Product Recommendation System

A smart product recommendation chatbot built with Streamlit and powered by AI. This application helps users find products based on their queries using natural language processing and provides intelligent recommendations.

## Features

* **Interactive Chat Interface** - ChatGPT-style conversational UI
* **Smart Product Search** - Keyword-based product matching
* **Price Filtering** - Find products within your budget
* **Rating-Based Sorting** - Get top-rated products first
* **AI-Powered Recommendations** - Using Groq's LLaMA model for intelligent suggestions
* **Product Analytics** - View total products and categories

## Tech Stack

* **Frontend** : Streamlit
* **AI Model** : Groq LLaMA 3.1
* **NLP** : Sentence Transformers, LangChain
* **Vector Database** : ChromaDB
* **Data Processing** : Pandas, NumPy

## Installation

### Prerequisites

* Python 3.8 or higher
* Groq API key ([Get it here](https://console.groq.com/))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Product_Recommendation_System.git
   cd Product_Recommendation_System
   ```
2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
5. **Download the embedding model** (optional)
   ```bash
   python download_model.py
   ```

## Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```
2. **Open your browser**
   The app will automatically open at `http://localhost:8501`
3. **Start chatting!**
   Try queries like:
   * "USB cable under 300"
   * "wireless headphones"
   * "gaming mouse"
   * "phone accessories"

## Project Structure

```
Product_Recommendation_System/
│
├── app.py                          # Main Streamlit application
├── download_model.py               # Script to download embedding models
├── requirements.txt                # Python dependencies
├── products_clean.csv              # Product dataset
├── config.pkl                      # Configuration file
├── .env                           # Environment variables (not in repo)
└── README.md                      # Project documentation
```

## Dataset

The product dataset (`products_clean.csv`) contains:

* Product names and descriptions
* Pricing information (original and discounted)
* Product ratings
* Categories
* Product details

## Features in Detail

### 1. Keyword Search

The system searches for products based on keywords in:

* Product names
* Product descriptions

### 2. Price Filtering

Automatically detects price constraints from queries:

* "under 300"
* "below 500"

### 3. AI Recommendations

Uses Groq's LLaMA 3.1 model to:

* Understand user intent
* Provide personalized recommendations
* Explain why products are suitable

## Configuration

### API Keys

The application requires a Groq API key. Add it to your `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### Model Settings

* **AI Model** : llama-3.1-8b-instant
* **Temperature** : 0.5 (balanced creativity)
* **Max Tokens** : 800
