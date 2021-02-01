import {
  Link
} from "react-router-dom";

function Login() {
  return (
    <div className="App">
      <div className="center">
        <div className="card" style={{ width: "350px" }}>
          <h2>Login</h2>
          <div style={{ height: "30px" }}></div>
          <form>
            <label htmlFor="email_input">Email</label>
            <input type="email" name="email" id="email_input" placeholder="email" />
            <div style={{ height: "10px" }}></div>

            <label htmlFor="password_input">Password</label>
            <input type="password" name="name" id="password_input" placeholder="password" />
            <div style={{ height: "10px" }}></div>

            <p className="small-text"><em>Don't have an account? <Link className="link" to="/register">Register</Link></em></p>
            <div style={{ height: "30px" }}></div>

            <input className="submit button" type="submit" value="Login" />
          </form>
        </div>
      </div>
    </div>
  )
}

export default Login;
