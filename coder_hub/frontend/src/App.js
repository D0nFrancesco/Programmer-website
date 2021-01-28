// React
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

// Pages
import Index from './pages/index.js';
import Projects from './pages/projects.js'
import Social from './pages/social.js'
import Login from './pages/login.js'
import Register from './pages/register.js'


// Components
import Header from './components/header.js';

// CSS
import './static/css/app.css';


function App() {
  return (
    <Router>
      <Header />
      <Switch>
        <Route path="/projects">
          <Projects />
        </Route>
        <Route path="/social">
          <Social />
        </Route>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/register">
          <Register />
        </Route>
        <Route path="/">
          <Index />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
