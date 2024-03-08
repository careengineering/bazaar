import streamlit as st
import os

def main():
    st.title("Fotoğraf Kaydetme Uygulaması")

    uploaded_file = st.file_uploader("Bir fotoğraf yükleyin", type=["jpg", "png"])

    if uploaded_file is not None:
        # Fotoğrafı geçici bir dosyaya kaydet
        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getvalue())

        st.success("Fotoğraf başarıyla yüklendi!")

        # Fotoğrafı istediğiniz bir dizine kaydedin
        save_path = os.path.join("kaydedilen_fotograflar", uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        st.success(f"Fotoğraf başarıyla {save_path} konumuna kaydedildi!")

if __name__ == "__main__":
    main()
