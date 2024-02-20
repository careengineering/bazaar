import streamlit as st
import datetime

# my lib
import items as it
import modal as md

today = datetime.datetime.now()

st.title("Pazar Alışverişi")

with (st.form("addpizza")):
    product_name = st.selectbox("Sebze/Meyve", it.fruit_and_vegetable_list, index=None, placeholder="...")
    product_unit_quantity = st.number_input("Miktar", value=1.0)
    product_unit = st.selectbox("Birim", it.pers, index=None, placeholder="...")
    product_unit_price = st.number_input("Fiyat")
    location = st.text_input("Konum")
    date = st.date_input("Tarih", value=today, format="DD.MM.YYYY")
    product_picture = st.file_uploader("Resim ekle")

    add_button = st.form_submit_button("Ekle")

    # 38°19′39″ N  26°46′21″ E

    if add_button:
        corrected_location = md.Modificators(location).correctionForLocation()

        created_product_picture_name = "img/" + md.Modificators(product_picture.name).changerForTurkishLetter()

        # open(product_picture_url, "wb").write(product_picture.read())

        st.write(product_name, " --- ",
                 product_unit_quantity, " --- ",
                 product_unit, " --- ",
                 product_unit_price, " --- ",
                 corrected_location, " --- ",
                 date, " --- ",
                 created_product_picture_name)
