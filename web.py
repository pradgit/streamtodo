import streamlit as st
import functionsfortodo as f
st.title("Pradnya Todo App with Streamlit")
st.subheader("Lets add some work to do")
st.write("Lets start with something")

todovar = f.get_todos()
def addtodo():
    todo = st.session_state["newtodo"] + "\n"
    todovar.append(todo)
    f.write_todos(todovar)

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

