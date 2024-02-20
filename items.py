import streamlit as st

fruit_and_vegetable_list = ["Enginar", "Patlıcan", "Kuşkonmaz", "Taze Fasulye",
                            "Brokoli", "Brüksel Lahanası", "Lahana", "Karnıbahar",
                            "Kereviz", "Mısır", "Salatalık", "Sarmısak", "Pırasa",
                            "Marul", "Mantar", "Soğan", "Bezelye", "Sivri Biber", "Kapya Biber",
                            "Patates", "Bal Kabağı", "Dolmalık Biber", "Ispanak", "Domates", "Elma",
                            "Şeftali", "Muz", "Böğürtlen", "Kiraz", "Üzüm", "Limon", "Portakal",
                            "Mandalina", "Vişne", "Avokado", "Ananas", "Siyah Üzüm", "Greyfurt",
                            "İncir", "Erik", "Armut", "Karpuz", "Kavun", "Kayısı", "Kivi", "Dut",
                            "Ahududu", "Havuç", "Hindistan Cevizi", "Kestane",
                            "Diğer"
                            ]

fruit_and_vegetable_list.sort()

if len(fruit_and_vegetable_list) == len(set(fruit_and_vegetable_list)):
    print("Ok")
else:
    for i in fruit_and_vegetable_list:
        print(i)

pers = ["kg", "g", "adet"]

