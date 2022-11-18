import React, {useState} from 'react';
import './App.css';

import {Login} from "./views/authentication/Login"
import {Register} from "./views/authentication/Register"
 
function App() {
  const[currentForm, setCurrentForm] = useState('register')
  
  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }
  return (
    <div className="App">
      
      
      {
        currentForm === "register" ? <Register onFormSwitch={toggleForm} /> : <Login onFormSwitch={toggleForm}/>
      }
       
    </div>
  );
}

export default App;
