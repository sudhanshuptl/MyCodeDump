import './styles.css';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

const root = document.getElementById('app-container')
ReactDOM.render(<App />, root)
//ReactDOM.render(<p>Hello, World</p>, root)
// this is same as below
//ReactDOM.render(React.createElement('p',null,'Welcome to ReactJS'),root)
// this seems very confusing to maintain and develop so facebbok create JSX

  
