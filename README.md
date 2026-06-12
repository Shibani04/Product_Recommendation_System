# Product Recommendation System

A smart product recommendation chatbot built with Streamlit and powered by AI. This application helps users find products based on their queries using natural language processing and provides intelligent recommendations.

## Project Highlights

- 1337 Products Indexed
- 9 Product Categories
- Conversational Shopping Assistant
- Budget-Aware Product Search
- AI-Assisted Recommendations using Groq LLaMA 3.1
- Streamlit-Based Interactive UI

## Features

* **Interactive Chat Interface** - ChatGPT-style conversational UI
* **Smart Product Search** - Keyword-based product matching
* **Price Filtering** - Find products within your budget
* **Rating-Based Sorting** - Get top-rated products first
* **AI-Powered Recommendations** - Using Groq's LLaMA model for intelligent suggestions
* **Product Analytics** - View total products and categories

## Application Screenshots

### Conversational Shopping Interface

<img width="1536" height="840" alt="image" src="https://github.com/user-attachments/assets/8fc6de71-b499-403f-b66b-b662ccfa09a9" />

The chatbot provides an interactive shopping experience with product analytics and suggested queries.

---

### AI-Powered Product Recommendations

<img width="1532" height="835" alt="image" src="https://github.com/user-attachments/assets/867db11b-e931-49e0-b819-c8dba68782f0" />

The system analyzes user requirements and recommends suitable products with explanations generated using Groq LLaMA 3.1.

---

### Product Search Example

<img width="1533" height="831" alt="image" src="https://github.com/user-attachments/assets/cf601bae-a44c-4ab2-8528-9978fc05a7fb" />

Users can search for products using natural language queries and receive ranked recommendations.

## Tech Stack

* **Frontend** : Streamlit
* **AI Model** : Groq LLaMA 3.1
* **Search Engine** : Intelligent Keyword-Based Product Search
* **Recommendation Logic** : Price Filtering & Rating-Based Ranking
* **Data Processing** : Pandas, NumPy

## Installation

### Prerequisites

* Python 3.8 or higher
* Groq API key ([Get it here](https://console.groq.com/))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shibani04/Product_Recommendation_System.git
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

### 3. AI-Assisted Recommendations

Uses Groq's LLaMA 3.1 model to:

* Analyze user shopping requirements
* Recommend suitable products from filtered results
* Generate natural language explanations

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

## My Contributions

- Built the Streamlit conversational shopping assistant
- Developed keyword-based product retrieval logic
- Implemented budget-aware product filtering
- Added rating-based product ranking
- Integrated Groq LLaMA 3.1 for intelligent recommendations
- Processed and analyzed the product dataset


