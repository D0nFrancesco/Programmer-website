import '../static/css/components/header.css'
import {
  Link
} from "react-router-dom";


function Header() {
	return (
		<header>
			<h1><Link to="/" className="no-link">CoderHub</Link></h1>
			<nav>
				<ul>
					<li><Link to="/">Home</Link></li>
					<li><Link to="/projects">Projects</Link></li>
					<li><Link to="/social">Social</Link></li>
				</ul>
			</nav>
			<ul className="login">
				<li><Link to="/login">Log In</Link></li>
				<li><Link to="/register">Register</Link></li>
			</ul>	
		</header>
	)
}

export default Header;
