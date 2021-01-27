import './static/css/app.css';
import './static/css/components.css';

function App() {
  return (
    <div className="App">
      <div className="card" style={{width: "500px"}}>
        <h3>Login</h3>
        <div style={{height: "10px"}}></div>
        <form>
          <label htmlFor="nameinput">Name</label>
          <input type="text" name="name" id="name_input" placeholder="name" />
        </form>
      </div>
    </div>
  );
}

export default App;
