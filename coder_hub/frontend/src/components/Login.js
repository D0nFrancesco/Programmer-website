import { FaGithub, FaGoogle } from 'react-icons/fa';
import '../static/login.css';

const Login = () => {
    return (        
        <div className="sign-in-container">
            <h3>Sign In</h3>
            <form method="POST" className="form">
                <div className="form-field">                    
                    <label className="label" htmlFor="name_input">Name</label>
                    <input className="input" type="text" name="name" id="name_input" placeholder="name" />
                </div>
                <div className="form-field">
                    <label className="label" htmlFor="password_input">Password</label>
                    <input className="input" type="password" name="name" id="password_input" placeholder="password" />
                </div>       

                <input id="submit" className="btn" type="submit" value="Sign In"/>
                <input className="btn btn-blue" type="button" value="Forgot Password"/>
                <p>Don't have an account <a href="#">Register</a></p>

            </form>
            {/* third party accounts */}
            <div className="third-party">
                <p>Sign in with one of 3rd party accounts</p>
                <button className="btn" id="google"><FaGoogle /> Sign in with Google</button>
                <button className="btn" id="github"><FaGithub /> Sign in with Github</button>
            </div>
        </div>
    )
}

export default Login
