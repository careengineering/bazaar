import streamlit as st


fruit_and_vegetable_list.sort()

if len(fruit_and_vegetable_list) == len(set(fruit_and_vegetable_list)):
    print("Ok")
else:
    for i in fruit_and_vegetable_list:
        print(i)

units = ["kg", "g", "adet"]

