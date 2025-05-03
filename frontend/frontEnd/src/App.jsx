import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import NavigationBar from './Components/NavigationBar/NavigationBar'
import { BrowserRouter } from 'react-router-dom'

function App() {
  return (
    <BrowserRouter>
      <NavigationBar />
    </BrowserRouter>
  )
}

export default App
