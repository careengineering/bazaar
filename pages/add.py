import streamlit as st
import datetime

# my libs
from tools import model
from tools import datas

# Preload
today = datetime.datetime.now()
database = model.Database(f"tools/{datas.database_name}")

st.title("Shopping")

with st.form("Add Product"):
    name = st.selectbox("Vegetables & Fruits", datas.name_list, index=None, placeholder="...")
    quantity = st.number_input("Quantity", value=1.0)
    unit = st.selectbox("Unit", datas.unit_list, index=0)
    price = st.number_input("Price")
    location = st.text_input("Location", value="38°19′39″ N  26°46′21″ E")
    date = st.date_input("Date", value=today, format="DD.MM.YYYY")
    picture = st.file_uploader("Add Pic")

    add_button = st.form_submit_button("Add")

    if add_button:
        if location is not None:
            corrected_location = model.Modificators(location).correctionForLocation()

        if picture is not None:
            created_picture_name = "img/" + str(date) + "-" + model.Modificators(
                picture.name).changerForTurkishLetter()
            open(created_picture_name, "wb").write(picture.read())
            save_picture_name = "http://localhost:8501/img/" + str(date) + "-" + model.Modificators(
                picture.name).changerForTurkishLetter()
        else:
            save_picture_name=""

        database.insertTable(datas.products_table,
                             [name, quantity, unit, price,
                              corrected_location,date, save_picture_name])

        st.success("Success")