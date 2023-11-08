import streamlit as st
from functions import get_todo,write_todo

def add_todo():
  todos=get_todo()
  todos.append((st.session_state["new_todo"]+'\n').capitalize())
  write_todo(todos)
  st.session_state["new_todo"]=""
st.title("Listify")
todos=get_todo()
for index,todo in enumerate(todos):
  checkbox=st.checkbox(todo,key=todo)
  if checkbox:
    todos.pop(index)
    del st.session_state[todo]
    write_todo(todos)
    st.experimental_rerun()
st.text_input(label="",placeholder="Type in new todo...",on_change=add_todo,key="new_todo")
