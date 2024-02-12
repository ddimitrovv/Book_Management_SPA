import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthProvider';
import styles from './Login.module.css';

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    await login(username, password, navigate);
  };

  return (
    <div className={styles['login-form']}>
      <div className={styles.form}>
        <h2>Login</h2>
        <div>
          <label>Username:</label>
          <input type="text" placeholder='Enter your username' value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div>
          <label>Password:</label>
          <input type="password" placeholder='Enter your password' value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button onClick={handleLogin}>Login</button>
      </div>
    </div>
  );
};

export default Login;
