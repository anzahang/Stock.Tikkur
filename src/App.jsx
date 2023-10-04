import { useState, useEffect, useRef } from 'react';
import Typed from 'typed.js'; // Import Typed.js
import logo from './assets/react.svg';
import './App.css';

function App(){
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const headerRef = useRef(null);
  useEffect(() => {
    const options = {
      strings: ['Stock.Tikkur'],
      typeSpeed: 100,
      backSpeed: 400,
      loop: false,
      showCursor: false, // Disable the typing cursor
    };
  
    const typed = new Typed(headerRef.current, options);
  
    return () => {
      typed.destroy();
    };
  }, []);
  
  
  const sendDataToPython = async () => {
    try {
      const response = await fetch('/api/receive_data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        console.log('Data sent successfully');
      } else {
        console.error('Data sending failed');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };
  return (
    <>
      <div className='container'>
        <img src={logo} alt="ALT Logo"/>
        <h1 ref={headerRef}>Stock-Tikkur</h1>
        <form onSubmit={e=>handleSubmit(e)}>
          <div className="inputContiner">
            <p>Email</p>
            <input 
            value={email} 
            onChange={(e)=> setEmail(e.target.value)} 
            type="text"
            />
          </div>
          <div className="inputContainer">
            <p>Password</p>
            <input 
            value={password}
            onChange={(e)=> setPassword(e.target.value)}
            type="password"
            />
          </div>
          <div className = "bottomForm">
            <button type ="submit" onClick={sendDataToPython}>Submit</button>
          </div>
        </form>
      </div>
    </>
  )
}

export default App;