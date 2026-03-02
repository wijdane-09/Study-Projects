/*const taskInput = document.getElementById('taskInput');
const taskList  = document.getElementById('taskList');
const addBtn  = document.getElementById('addBtn');
const clearCompletedBtn  = document.getElementById('clearCompleted');

addBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', function(e) {
  if (e.key === 'Enter') {
    addTask();
  }
});

clearCompletedBtn.addEventListener('click', function() {
  const completedTasks = document.querySelectorAll('.completed');
  completedTasks.forEach(li => li.remove());
});

function addTask() {
  const text = taskInput.value.trim();
  if (text === '') return;

  const li = document.createElement('li');

  const span = document.createElement('span');
  span.textContent = text;
  li.appendChild(span);

  // Toggle completed
  li.addEventListener('click', function(e) {
    if (e.target.tagName === "BUTTON") return;
    li.classList.toggle('completed');
  });

  // Edit button
  const editBtn = document.createElement('button');
  editBtn.textContent = '✏️';

  editBtn.addEventListener('click', function(e) {
    e.stopPropagation();

    if (editBtn.textContent === '✏️') {
      // turn text into input
      const input = document.createElement('input');
      input.type = 'text';
      input.value = span.textContent;

      li.insertBefore(input, span);
      li.removeChild(span);

      editBtn.textContent = 'Save';
      
    } else {
      // save edited text
      const input = li.querySelector('input');
      span.textContent = input.value.trim() || span.textContent;

      li.insertBefore(span, input);
      li.removeChild(input);

      editBtn.textContent = '✏️';
    }
  });

  // Delete button
  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = '❌';

  deleteBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    li.remove();
  });

  li.appendChild(editBtn);
  li.appendChild(deleteBtn);
  taskList.appendChild(li);

  taskInput.value = '';
}
*/