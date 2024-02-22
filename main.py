import streamlit as st
import datetime

# my libs
from tools import controller
from tools import modal

today = datetime.datetime.now()

st.title("Pazar Alışverişi")

with (st.form("addpizza")):
    product_name = st.selectbox("Sebze/Meyve", controller.products_name_table, index=None, placeholder="Seç")
    product_unit_quantity = st.number_input("Miktar", value=1.0)
    product_unit = st.selectbox("Birim", it.pers, index=None, placeholder="Seç")
    product_unit_price = st.number_input("Fiyat")
    product_location = st.text_input("Konum",value="38°19′39″ N  26°46′21″ E")
    product_unit_price_date = st.date_input("Tarih", value=today, format="DD.MM.YYYY")
    product_picture = st.file_uploader("Resim ekle")

    add_button = st.form_submit_button("Ekle")

    if add_button:
        corrected_product_location = modal.Modificators(product_location).correctionForLocation()

        created_product_picture_name = "img/" + modal.Modificators(product_picture.name).changerForTurkishLetter()

        # open(product_picture_url, "wb").write(product_picture.read())

        st.write(product_name, " --- ",
                 product_unit_quantity, " --- ",
                 product_unit, " --- ",
                 product_unit_price, " --- ",
                 corrected_product_location, " --- ",
                 product_unit_price_date, " --- ",
                 created_product_picture_name)
