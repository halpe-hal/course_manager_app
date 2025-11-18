# main.py

import streamlit as st
from modules import course_master, course_reservation, course_progress_view

def main():
    st.set_page_config(page_title="コース進行管理システム", layout="wide")

    st.title("コース進行管理システム")

    menu = st.sidebar.radio(
        "メニュー",
        [
            "1. コースマスタ管理",
            "2. コース予約登録",
            "3. コース進行ボード",
            "4. 調理済み一覧",
            "5. 配膳済み一覧",
        ]
    )

    if menu == "1. コースマスタ管理":
        course_master.show()
    elif menu == "2. コース予約登録":
        course_reservation.show()
    elif menu == "3. コース進行ボード":
        course_progress_view.show_board()
    elif menu == "4. 調理済み一覧":
        course_progress_view.show_cooked_list()
    elif menu == "5. 配膳済み一覧":
        course_progress_view.show_served_list()

if __name__ == "__main__":
    main()
