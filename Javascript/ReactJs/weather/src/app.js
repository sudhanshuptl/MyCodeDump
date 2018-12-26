import './styles.css';
import React from 'react';
import ReactDOM from 'react-dom';

const root = document.getElementById('app-container')

//ReactDOM.render(<p>Hello, World</p>, root)
// this is same as below
ReactDOM.render(React.createElement('p',null,'Welcome to ReactJS'),root)
  
