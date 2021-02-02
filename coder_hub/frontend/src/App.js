// React
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

// Pages
import Index from './pages/index.js';
import Projects from './pages/projects.js';
import Social from './pages/social.js';
import Login from './pages/login.js';
import Register from './pages/register.js';
import UserPage from './pages/user.js';
import Project from './pages/project.js'

// Components
import Header from './components/header.js';

// CSS
import './static/css/app.css';


function App() {
  return (
    <Router>
      <Header />
      <Switch>
        {/* Dynamic routes */}
        <Route exact path="/u/:username" component={ UserPage } />
        <Route exact path="/p/:projectid" component={ Project } />

        {/* Pages */}
        <Route path="/projects" component={ Projects }  />
        <Route path="/social" component={ Social} />
        <Route path="/login" component={ Login } />
        <Route path="/register" component={ Register} />

        {/* Index */}
        <Route path="/" component={ Index } />
      </Switch>
    </Router>
  );
}

export default App;
