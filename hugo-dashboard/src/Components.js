import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link} from 'react-router-dom';

export class Pub extends Component {
	constructor() {
		super();
		this.state = {
			title: '',
			year: ''
		};
		this.handleChange = this.handleChange.bind(this);
	}

	handleChange(event) {
		this.setState({ [event.target.name]: event.target.value});
	}

	render() {
		return (
				<form>
				<label> Title: </label>
				<input type="text" name="title" onChange={this.handleChange} /> <br />
				<label> Year: </label>
				<input type="text" name="year" onChange={this.handleChange} /> <br />
				<input type="submit" value="Submit" />
				<Link to="/"><button>Back</button></Link>
				</form>
				);
	}
}

export class Intro extends Component {
	  constructor() { 
			super();              
			this.state = {              
				name: '',                    
				homepage: ''                      
			};                  
			
			this.handleChange = this.handleChange.bind(this);
		}
		      
		handleChange(event) {           
			this.setState({ [event.target.name]: event.target.value});
		}
			        
		render() {              
			return (                          
					<form>                                  
					<label> Name: </label>                                         
					<input type="text" name="name" onChange={this.handleChange} /> <br />
					<label> Homepage: </label>                                                          
					<input type="text" name="homepage" onChange={this.handleChange} /> <br />
					<input type="submit" value="Submit" />
					<Link to="/"><button>Back</button></Link>
					</form>                                                                     
					);        
		}
}



