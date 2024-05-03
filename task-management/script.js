firebase.initializeApp({
    apiKey: "AIzaSyC5Gq3QzNI8r49adn9ica-CjNapRSL1zv8",
    authDomain: "plp-app-a9a85.firebaseapp.com",
    projectId: "plp-app-a9a85",
    storageBucket: "plp-app-a9a85.appspot.com",
    messagingSenderId: "165062626188",
    appId: "1:165062626188:web:ba1a20ea4708e0db3624a9",
    measurementId: "G-0PEM9EB35B"
});

const db = firebase.firestore();

// function to add tasks
function addTask(){
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value.trim();
    if(task !== ""){
        db.collection('tasks').add({
            task: task,
            timestamp: firebase.firestore.FieldValue.serverTimestamp()
        });
        taskInput.value = "";
        console.log("Task added.");
    }
}

function renderTasks(doc){
    const taskList = document.getElementById('task-list');
    const taskItem = document.createElement('li');
    taskItem.className = 'task-item';
    taskItem.innerHTML = `
        <span>${doc.data().task}</span>
        <button onclick="deleteTask('${doc.id}')">Delete</button>
    `;
    taskList.appendChild(taskItem);
}

db.collection("tasks")
    .orderBy('timestamp', "desc")
    .onSnapshot(snapshot => {
        const changes = snapshot.docChanges();
        changes.forEach(change => {
            if(change.type === "added"){
                renderTasks(change.doc);
            }
        });
    });

function deleteTask(id){
    db.collection('tasks').doc(id).delete();
    location.reload();
}