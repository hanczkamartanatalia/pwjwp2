import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

st.set_page_config(page_title="Sprzedaż", layout="wide")


def get_connection():
    return sqlite3.connect("sales.db", check_same_thread=False)


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            quantity INTEGER,
            price REAL,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()


init_db()

st.sidebar.header("➕ Dodaj nową sprzedaż")
with st.sidebar.form("add_sale_form"):
    product = st.text_input("Produkt")
    quantity = st.number_input("Ilość", min_value=1, value=1)
    price = st.number_input("Cena (za sztukę)", min_value=0.0, value=1.0)
    sale_date = st.date_input("Data", value=date.today())
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        conn = get_connection()
        conn.execute(
            "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
            (product, quantity, price, sale_date.isoformat())
        )
        conn.commit()
        conn.close()
        st.sidebar.success("✅ Sprzedaż dodana!")
        st.balloons()

conn = get_connection()
df = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()

df["date"] = pd.to_datetime(df["date"])

st.title("📊 Dashboard Sprzedaży")
products = df["product"].unique().tolist()
selected_product = st.selectbox("Filtruj po produkcie", ["Wszystkie"] + products)

if selected_product != "Wszystkie":
    df = df[df["product"] == selected_product]

st.subheader("📋 Tabela danych")
st.dataframe(df)

st.subheader("📈 Sprzedaż dzienna (wartość)")
df["total_value"] = df["quantity"] * df["price"]
daily_sales = df.groupby("date")["total_value"].sum().reset_index()

fig1, ax1 = plt.subplots()
sns.lineplot(data=daily_sales, x="date", y="total_value", marker="o", ax=ax1)
ax1.set_title("Sprzedaż dzienna")
ax1.set_ylabel("Wartość sprzedaży")
st.pyplot(fig1)

st.subheader("📦 Suma sprzedanych produktów wg typu")
product_sum = df.groupby("product")["quantity"].sum().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(data=product_sum, x="product", y="quantity", ax=ax2)
ax2.set_title("Łączna liczba sprzedanych sztuk wg produktu")
ax2.set_ylabel("Sztuki")
ax2.set_xlabel("Produkt")
st.pyplot(fig2)

if st.checkbox("🎉 Pokaż animację (st.balloons)"):
    st.balloons()
