import pandas as pd
import streamlit as st
import numpy as np
import datetime

# my libs
from tools import model
from tools import datas

# Preload
today = datetime.datetime.now()
database = model.Database(f"tools/{datas.database_name}")

st.title("List")

df = pd.DataFrame(database.getTableSortByColumnName(datas.products_table,"date"))


st.dataframe(
    df,
    column_config={
        1: "Name",
        2: "Quantity",
        3: "Unit",
        4: st.column_config.NumberColumn(
            "Price",
            format="₺ %.2f"
        ),
        5: "Location",
        6: st.column_config.DateColumn(
            "Date",
            format="DD.MM.YYYY"
        ),
        7: st.column_config.ImageColumn(
            "Pic"
        )
    },
    hide_index=True,
    use_container_width= True
)