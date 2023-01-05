import streamlit as st
import functions

todos = functions.get_todos()

# The session state is a type which is similar to a dictionary and is updated evey time we press enter after
# updating the values
# the session_state will have key value pair for those states which has a key

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # we are accessing the new_todo key to get the corresponding value
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To Do App")
st.subheader("List down things to be done:")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # the key here is set to todo, which have key value pair as below
    # {
    #  "Work very hard": false
    #  "Hi": false
    #  "Code untill you get a job": false
    #  "Practise SQLReturn the book": false
    #  "new_todo": ""
    #  "Play cricket": false
    # "Submit docs": false
    # "Throw the trash": false
    # "Go to the gym": false
    # "Sleep": false
    # }
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



# the on_change function will be called every time there is a change in state of the text  field
# and we access the corresponding value from the session_state type (similar to a dict)
st.text_input(label="", placeholder="Enter a new to do...", on_change=add_todo, key="new_todo")


# st.session_state