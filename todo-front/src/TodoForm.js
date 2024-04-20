// TodoForm.js
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom'; // Import useNavigate
import axios from 'axios';

const TodoForm = () => {
  const navigate = useNavigate();
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const { id } = useParams();

  useEffect(() => {
    if (id) {
      axios.get(`http://localhost:8000/todo/${id}`)
        .then(response => {
          setTitle(response.data.title);
          setDescription(response.data.description);
        })
        .catch(error => console.error(error));
    }
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = { title, description };

    try {
      if (id) {
        await axios.patch(`http://localhost:8000/todo/${id}`, data);
      } else {
        await axios.post('http://localhost:8000/todo/', data);
      }
      navigate('/'); // Use navigate to redirect to a different route
    } catch (error) {
      console.error(error);
    }
  };


  return (
    <div className="todo-form-container">
      <h1 className='title-page1'>{id ? 'Edit Todo' : 'Add Todo'}</h1>
      <form onSubmit={handleSubmit} className="todo-form">
        <input type="text" placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} className="todo-input" />
        <input type="text" placeholder="Description" value={description} onChange={e => setDescription(e.target.value)} className="todo-input" />
        <button type="submit" className="add-todo-b">{id ? 'Update Todo' : 'Add Todo'}</button>
      </form>
    </div>
  );
};

export default TodoForm;
