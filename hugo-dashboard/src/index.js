import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './index.css';
import App from './App';
import {Pub, Intro} from './Components';



ReactDOM.render(
		<Router>
			<div>
			<Route exact path="/" component={App} />
			<Route path="/publications" component={Pub} />
			<Route path="/intro" component={Intro} />
			</div>
		</Router>,
		document.getElementById('root'));
