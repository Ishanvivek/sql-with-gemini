from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


def get_gemini_responce(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close

    for row in rows:
        print(row)
        return rows



prompt = [ """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
For example:
Example 1 - How many entries of records are present? The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
Example 2 - Tell me all the students studying in Data Science class? The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data Science";
Also, the SQL code should not have ** at the beginning or end, and the word SQL should not be in the output.
"""
]


st.set_page_config(page_title="I CAN RETRIEVE ANY SQL QUERY")
st.header("SQL with the help of google gemini")

question=st.text_input("Search: ",key="input")

submit=st.button("Ask Your Query")

if submit: 
    response=get_gemini_responce(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)


