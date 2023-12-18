# Semantic Search Engine
This is an end-to-end search engine that is designed to interact with a MySQL database. This engine allows users to ask questions in natural language. It then translates these questions into SQL queries and executes them on the MySQL database to retrieve answers. We're implementing this technology at AtliQ Tees, a T-shirt store that manages its inventory, sales, and discount data using a MySQL database.

## Index
1. [Background](#background)
2. [Preview](#preview)
3. [Installation](#installation)
4. [Run Locally](#run-locally)
5. [Sample Queries](#sample-queries)
6. [Repository Structure](#repository-structure)
7. [About the author](#about-the-author)

## Background
AtliQ Tees is a hypothetical T-shirt store that sells T-shirts from 4 brands: Adidas, Nike, Levi’s and Van Heusen. The data related to the store’s inventory, sales and discounts is stored in a MySQL database. Here we are building an LLM-based query system that uses the below-given technologies to answer questions based on the database. In the UI, the store manager can type questions in natural language, and the system will generate the answers:
* LangChain as our framework
* Google PaLM
* Few-shot learning
* Hugging Face for embedding generation
* ChromaDB as vector store
* Streamlit for UI


## Preview

## Installation

1. Create a local copy of this repository on your machine:
```
git clone https://github.com/ayucd/llm-on-sql.git
```
2. Go to the project directory:
```
cd llm-on-sql
```
3. Install the required dependencies using pip:
```
pip install -r requirements.txt
```
4. Acquire an API key through makersuite.google.com and put it in the .env file:
```
GOOGLE_API_KEY="your_api_key_here"
```
5. Run database/db_creation_atliq_t_shirts.sql in your MySQL workbench to set up the database.

## Run Locally

1. Run the Stramlit UI for the engine by using:
```
streamlit run main.py
```
2. The web app will then open in your browser where you can query the SQL database to get numerical answers!

## Sample Queries













