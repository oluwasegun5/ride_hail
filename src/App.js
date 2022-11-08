import React, {useState} from 'react';
import logo from './logo.svg';
import './App.css';
import {Landing} from "./Landing"
import {Login} from "./Login"
import {Register} from "./Register"
 
function App() {
  const[currentForm, setCurrentForm] = useState('register')
  
  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }
  return (
    <div className="App">
      
      
      {
        currentForm === "login" ? <Login onFormSwitch={toggleForm} /> : <Register onFormSwitch={toggleForm}/>
      }
       
    </div>
  );
}

export default App;
