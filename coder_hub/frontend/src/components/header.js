import '../static/css/components/header.css'
import {
  Link
} from "react-router-dom";


function Header() {
	return (
		<header>
			<nav>
				<nav>
					<h1><Link to="/" className="no-link">CoderHub</Link></h1>
					<ul>
						<li><Link to="/">Home</Link></li>
						<li><Link to="/projects">Projects</Link></li>
						<li><Link to="/social">Social</Link></li>
					</ul>
				</nav>
				<ul>
					<li><Link to="/login">Log In</Link></li>
					<li><Link to="/register">Register</Link></li>
				</ul>
			</nav>
		</header>
	)
}

export default Header;
