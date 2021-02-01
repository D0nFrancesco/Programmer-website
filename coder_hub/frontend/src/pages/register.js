import {
  Link
} from "react-router-dom";

function Register() {
  return (
    <div className="App">
      <div className="center">
        <div className="card" style={{ width: "350px" }}>
          <h2>Register</h2>
          <div style={{ height: "30px" }}></div>
          <form>
            <label htmlFor="name_input">Name</label>
            <input type="text" name="name" id="name_input" placeholder="name" />
            <div style={{ height: "10px" }}></div>

            <label htmlFor="email_input">Email</label>
            <input type="email" name="email" id="email_input" placeholder="email" />
            <div style={{ height: "10px" }}></div>

            <label htmlFor="password_input">Password</label>
            <input type="password" name="password" id="password_input" placeholder="password" />
            <div style={{ height: "10px" }}></div>

            <label htmlFor="confirm_password_input">Confirm password</label>
            <input type="password" name="confirm_password" id="confirm_password_input" placeholder="password" />
            <div style={{ height: "10px" }}></div>

            <p className="small-text"><em>When registering you agree to our terms of service</em></p>
            <div style={{ height: "10px" }}></div>
            <p className="small-text"><em>Already have an account? <Link to="/login" className="link">Login</Link></em></p>

            <div style={{ height: "30px" }}></div>

            <input className="submit button" type="submit" value="Register" />
          </form>
        </div>
      </div>
    </div>
  )
}

export default Register;
