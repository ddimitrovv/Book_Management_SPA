import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthProvider';
import styles from './Register.module.css';

const Register = () => {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      setPasswordError("Passwords don't match");
      return;
    }

    setPasswordError('');

    await register(username, email, password, navigate);
  };

  return (
    <div className={styles['register-form']}>
      <div className={styles.form}>
        <h2>Register</h2>
        <div>
          <label>Username:</label>
          <input type="text" placeholder='Enter your username' value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div>
          <label>Email:</label>
          <input type="email" placeholder='Enter your email' value={email} onChange={(e) => setEmail(e.target.value)} />
        </div>
        <div>
          <label>Password:</label>
          <input type="password" placeholder='Enter your password' value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <div>
          <label>Confirm Password:</label>
          <input type="password" placeholder='Confirm your password' value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
          {passwordError && <p className="error">{passwordError}</p>}
        </div>
        <button onClick={handleRegister}>Register</button>
      </div>
    </div>
  );
};

export default Register;
