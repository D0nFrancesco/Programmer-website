// CSS
import '../static/css/components/form.css';
import '../static/css/components/card.css';

function Index() {
    return (
        <div className="App">
            <div className="card" style={{width: "500px"}}>
            <h3>Login</h3>
            <div style={{height: "10px"}}></div>
            <form>
                <label htmlFor="name_input">Name</label>
                <input type="text" name="name" id="name_input" placeholder="name" />
                <div style={{height: "10px"}}></div>

                <label htmlFor="password_input">Password</label>
                <input type="password" name="name" id="password_input" placeholder="password" />
                <div style={{height: "10px"}}></div>

                <input className="submit button" type="submit" value="Login"/>
            </form>
            </div>
        </div>
    )
}

export default Index;
