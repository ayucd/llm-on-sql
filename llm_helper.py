from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import pymysql
import mysql.connector
import sqlalchemy as sal
from sqlalchemy import create_engine, MetaData, Table
import pandas as pd
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from few_shots import few_shots
from secret_key import GOOGLE_API_KEY


def get_few_shot_db_chain():
    llm = GooglePalm(google_api_key=GOOGLE_API_KEY, temperature=0.2)

    db_host = 'localhost'
    db_port = 3306
    db_user = 'root'
    db_password = 'root'
    db_name = 'atliq_tshirts'

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],  # These variables are used in the prefix and suffix
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)

    return chain

if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("How many total t shirts are left in total in stock?"))
