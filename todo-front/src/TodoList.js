// TodoList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom'; 

const TodoList = () => {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/todo/')
      .then(response => setTodos(response.data))
      .catch(error => console.error(error));
  }, []);

  const deleteTodo = (id) => {
    axios.delete(`http://localhost:8000/todo/${id}`)
      .then(() => {
        setTodos(todos.filter(todo => todo.id !== id));
      })
      .catch(error => console.error(error));
  };

  const markTodoDone = (id) => {
    axios.patch(`http://localhost:8000/todo/${id}`, { status: "Done" })
      .then(() => {
        setTodos(todos.map(todo => todo.id === id ? { ...todo, status: "Done" } : todo));
      })
      .catch(error => console.error(error));
  };

  return (
    <div className="todo-list-container">
      <h1 className='title-page'>Todo List</h1>
      <Link to="/add" className="add-todo-link"><div className="add-todo-btn">Add Todo</div></Link>
      <ul className="todo-list">
        {todos.map(todo => (
          <li key={todo.id} className={`todo-item ${todo.status === "Done" ? "done" : ""}`}>
            <span className={`todo-title  ${todo.status === "Done" ? "done1" : ""}`}>{todo.title}</span>
            <div className="todo-actions">
              <Link to={`/edit/${todo.id}`} className={`list-button edit-todo-btn ${todo.status === "Done" ? "disabled donebtn" : ""}`}><button className={`list-button edit-todo-btn ${todo.status === "Done" ? "disabled donebtn" : ""}`} disabled={todo.status === "Done"}><i className="icon edit-icon"></i>Edit</button></Link>
              <button onClick={() => markTodoDone(todo.id)} className={`list-button done-todo-btn ${todo.status === "Done" ? "disabled donebtn" : ""}`} disabled={todo.status === "Done"}><i className="icon done-icon"></i>Done</button>
              <button onClick={() => deleteTodo(todo.id)} className="list-button delete-todo-btn"><i className="icon delete-icon"></i>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
