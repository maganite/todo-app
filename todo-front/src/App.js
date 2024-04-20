// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Import BrowserRouter, Routes, and Route
import TodoList from './TodoList';
import TodoForm from './TodoForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TodoList />} />
        <Route path="/add" element={<TodoForm />} />
        <Route path="/edit/:id" element={<TodoForm />} />
      </Routes>
    </Router>
  );
}

export default App;
