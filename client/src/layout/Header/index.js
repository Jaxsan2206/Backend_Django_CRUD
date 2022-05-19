import React from 'react'
import { NavLink } from 'react-router-dom'

function Header() {
  return (
    <nav>
        <NavLink to='/'>Home</NavLink>
        <NavLink to='/register'>Register</NavLink>
        <NavLink to='/login'>Login</NavLink>
    </nav>
  )
}

export default Header