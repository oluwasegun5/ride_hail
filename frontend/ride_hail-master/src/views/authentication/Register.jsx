import React, { useState } from 'react';

export const Register = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);

    }
    return[
        <div className='auth-form-container'>
            <form classname="register-form" onSubmit={handleSubmit}>
                <div className='register-box'>
                    <p>Let's get to know you.</p>
                    <input value={firstName} onChange={(e) => setFirstName(e.target.value)} type="name" name="firstName" id='firstName' placeholder='   first name'></input>
                    <input value={lastName} onChange={(e) => setLastName(e.target.value)} type="name" name="lastName" id='lastName' placeholder='   last name'></input>
                    <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="   email" id="email" name="email"/>
                    <input value={pass} onChange={(e) => setPass(e.target.value)}type="password" placeholder="   password" id="    password" name="password"/>
                    <div className='google-signup'>

                    </div>
                    <div className='button-link'>
                        <button type="submit">Sign up</button>
                        <a className="login-link" onClick={ () => props.onFormSwitch('login') }>Already have an account? Login</a>

                    </div>

                </div>

            </form>

        </div>
    ]

}