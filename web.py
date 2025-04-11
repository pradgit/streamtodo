import streamlit as st
import functionsfortodo as f
import pandas as pn

#add streamlit python files in pages folder
#pradtodoliststreamlit

#layout adjustment
st.set_page_config(layout="wide")

st.title("Pradnya Todo App with Streamlit")
st.write("Start adding Pending tasks")

#common variable to store the TODOS
todovar = f.get_todos()
print(todovar)
print('Hello')


def addtodo():
    todo = st.session_state["newtodo"] + "\n"
    todovar.append(todo)
    f.write_todos(todovar)
    st.session_state["newtodo"] = ""

#st.checkbox("Buy grocery for weekend")
for index, work in enumerate(todovar):
    checkedtodo = st.checkbox(work,key=work)
    if checkedtodo:
        todovar.pop(index)
        f.write_todos(todovar)
        del st.session_state[work]
        #rerun the checkbox with new values
        st.experimental_rerun()

#onchange call addtodo and key to identify
st.text_input(label ="Enter more todo's:",placeholder="Add here",on_change=addtodo,key='newtodo')

