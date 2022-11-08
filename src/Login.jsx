import React, {useState} from'react'
export const Login = (props) => {
    const[email,setEmail] = useState('');
    const[pass, setPass] = useState('');
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }
    return(
        <div className='auth-form-container'>
            <form classname="login-form" onSubmit={handleSubmit}>
            
                <div className='login-box'>
                <p>Sign in to continue.</p>
                    <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="   email" id="email" name="email"/>
                    <input value={pass} onChange={(e) => setPass(e.target.value)}type="password" placeholder="   password" id="password" name="password"/>
                    
                    <div className='button-link'>
                    <button className="login-button"type="submit">Log in</button>
                    <a className="login-link" onClick={ () => props.onFormSwitch('register') }>Don't have an account? Register</a>

                    </div>
                    

                </div>
                
            </form>

        </div>
    )
}