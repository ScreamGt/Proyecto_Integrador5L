import React from 'react'
import './Login.css'
import '../../App.css'
import { Link } from 'react-router-dom';
//importar nuestros recursos
import video from '../../LoginAssets/Login-video.webm'
import logo from '../../LoginAssets/logo.png'
//importar iconos de react
import { FaUserShield } from "react-icons/fa";
import { BsFillShieldLockFill } from "react-icons/bs";
import { AiOutlineSwapRight } from "react-icons/ai";

const Login = () => {
  return (
    <div className='loginPage flex'>
      <div className="container flex">

        <div className="videoDiv">
          <video src={video} autoPlay muted loop></video>

          <div className="textDiv">
            <h2 className='tittle'>Gestiona tus productos con la mejor herramienta</h2>
            <p>Solo productos naturales!</p>
          </div>

          <div className="footerDiv flex">
            <span className="text">Aun no tienes una cuenta?</span>
            <Link to = {'/register'}>
            <button className='btn'>Sing up</button>
            </Link>
          </div>

        </div>

        <div className="formDiv flex">
          <div className="headerDiv">
            <img src= {logo} alt="Logo Image" />
            <h3>Bienvenido de vuelta!</h3>
          </div>

          <form action="" className='form grid'>
            <span className='showMessage'>Estado de inicio de sesion</span>

            <div className="inputDiv">
              <label htmlFor="username">Username</label>
              <div className="input flex">
                <FaUserShield className ='icon'/>
                <input type="text" id="username" placeholder='Enter Username' />
              </div>
            </div>

            <div className="inputDiv">
              <label htmlFor="password">Password</label>
              <div className="input flex">
                <BsFillShieldLockFill className ='icon'/>
                <input type="text" id="password" placeholder='Enter Password' />
              </div>
            </div>

            <button type='submit' className='btn flex'>
              <span>Login</span>
              <AiOutlineSwapRight className='icon' />
            </button>

            <sapn className="frogotPassword">
              Olvidaste tu contraseña <a href="">Click Aqui</a>
            </sapn>
          </form>

        </div>

      </div>
    </div>
  )
}

export default Login