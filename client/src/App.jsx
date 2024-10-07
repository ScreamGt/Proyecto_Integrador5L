import './App.css'
import Dashboard from './components/Dashboard/Dashboard'
import Login from './components/Login/Login'
import Register from './components/Register/Register'

//import React router dom
import{
  createBrowserRouter,
  RouterProvider
} from 'react-router-dom'

//Para crear un router
const router = createBrowserRouter([
  {
    path: '/',
    element: <div><Login/></div>
  },
  {
    path: '/register',
    element: <div><Register/></div>
  },
  {
    path: '/dashboard',
    element: <div><Dashboard/></div>
  },
])

function App() {

  return (
    <dev>
      <RouterProvider router = {router}/>
    </dev>
  )
}

export default App
