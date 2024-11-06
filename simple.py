import streamlit as st
import sqlite3

st.set_page_config(page_title="Login Page", layout="centered")
st.title("Welcome to the Login Page")

def get_conn():
    conn = sqlite3.connect("none.db")
    conn.row_factory = sqlite3.Row
    return conn


st.header("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("print"):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    data = [dict(row) for row in rows]
    st.write(data)  # This will display a list of dictionaries with your data


if st.button("Login"):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        st.success("Login successful! Redirecting to the dashboard...")
    else:
        st.error("Invalid credentials. Please try again.")
if st.button("register"):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
if 'user_logged_in' in st.session_state and st.session_state['user_logged_in']:
    st.title("Welcome to the Dashboard")
    st.write("Here is your dashboard content...")
