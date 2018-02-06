import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link} from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import {Pub, Intro} from './Components';


class App extends Component {

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
				<body> 
					 <div className="pub-form">
					 		<Link to="/publications"><button>Add Publication</button></Link>
							<Link to="/intro"><button>Add Introduction</button></Link>
					 </div>
					 <div> 
					 	<p> Hola 2</p>
					 </div>
				</body>
			</div>
    );
  }
}


export default App;

