from js import document #type: ignore

text = document.getElementById("Text")
taskList = document.getElementById("Tasklist")
tasks = []

def addTasks(event):
    event.preventDefault()
    userInput = document.getElementById("UserInput").value

    tasks.append(userInput)

    document.getElementById("UserInput").value = ""
        
    listItem = document.createElement('li')
    listItem.setAttribute('contenteditable', 'true')
    checkBox = document.createElement('input')
    checkBox.className = "CheckBox"
    checkBox.setAttribute('type', 'checkbox')
    listItem.textContent = str(tasks[-1])
    #listItem.appendChild(checkBox)
    listItem.prepend(checkBox)
    taskList.appendChild(listItem)

    

addButton = document.getElementById("AddButton").addEventListener("click", addTasks)
