import streamlit as st

# Inicjalizacja listy magazynu
# Używamy zwykłej globalnej listy, ponieważ Streamlit bez stanu sesji
# będzie ją resetował przy każdym przeładowaniu/interakcji.
# Jest to celowe w kontekście Twojego zapytania (bez sesji),
# choć w praktycznej aplikacji Streamlit do magazynu użylibyśmy st.session_state
# lub bazy danych.
if 'warehouse' not in globals():
    warehouse = ["Laptop (Model X1)", "Monitor (27 cali)", "Klawiatura mechaniczna"]

def add_item(item_name):
    """Dodaje produkt do magazynu."""
    if item_name:
        warehouse.append(item_name)
        st.success(f"Dodano: **{item_name}** do magazynu.")
    else:
        st.error("Nazwa produktu nie może być pusta.")

def remove_item(item_name):
    """Usuwa produkt z magazynu."""
    try:
        warehouse.remove(item_name)
        st.warning(f"Usunięto: **{item_name}** z magazynu.")
    except ValueError:
        st.error(f"Błąd: Produkt **{item_name}** nie został znaleziony w magazynie.")

# --- Interfejs użytkownika Streamlit ---

st.title("📦 Prosty Magazyn (Streamlit + Lista)")
st.caption("Uwaga: Ten magazyn jest resetowany po każdej interakcji, ponieważ nie używa `st.session_state`.")

# Sekcja Dodawania Produktu
st.header("➕ Dodaj Produkt")
with st.form("add_form", clear_on_submit=True):
    new_item = st.text_input("Nazwa produktu do dodania:", key="new_item_input")
    submitted_add = st.form_submit_button("Dodaj do Magazynu")

    if submitted_add:
        add_item(new_item)

# Separator
st.markdown("---")

# Sekcja Usuwania Produktu
st.header("➖ Usuń Produkt")
# Używamy selectbox, aby łatwo wybrać produkt do usunięcia
if warehouse:
    item_to_remove = st.selectbox("Wybierz produkt do usunięcia:", warehouse, key="remove_item_select")
    submitted_remove = st.button("Usuń Wybrany Produkt")

    if submitted_remove:
        remove_item(item_to_remove)
else:
    st.info("Magazyn jest pusty, nie można nic usunąć.")

# Separator
st.markdown("---")

# Sekcja Wyświetlania Stanu Magazynu
st.header("📊 Aktualny Stan Magazynu")
if warehouse:
    st.dataframe(
        data={"Indeks": range(len(warehouse)), "Nazwa Produktu": warehouse},
        use_container_width=True,
        hide_index=True
    )
    st.metric("Liczba różnych produktów:", len(warehouse))
else:
    st.info("Magazyn jest obecnie pusty.")
