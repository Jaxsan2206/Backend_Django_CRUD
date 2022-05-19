import React, {useState} from 'react'

function Register() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [confirmPass, setConfirmPass] = useState('')

    const handleUser = (e) => {
        setUsername(e.target.value)
    }
    const handlePass = (e) => {
        setPassword(e.target.value)
    }
    const handleCPass = (e) => {
        setConfirmPass(e.target.value)
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const options = {
            method : 'POST', 
            body: JSON.stringify({username: username, password: password, password_confirmation: confirmPass}),
            headers: {'Content-Type': 'application/json'}
        }
        const response = await fetch('http://127.0.0.1:8000/api/register/', options)
        const response_json = await response.json()
        console.log(response_json)
    }

  return (
    <>
    <form onSubmit={handleSubmit}>
        <label htmlFor='username'>Enter Username: </label>
        <input type='text' id="username" onChange={handleUser}></input>
        <label htmlFor='password'>Enter Password: </label>
        <input type='password' id='password' onChange={handlePass}></input>
        <label htmlFor='confirm_password'>Confirm Password: </label>
        <input type='password' id='confirm_password'onChange={handleCPass}></input>
        <input type='submit' value='Sign up!'></input>
    </form>
    </>
  )
}

export default Register