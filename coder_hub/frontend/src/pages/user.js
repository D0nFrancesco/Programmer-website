import '../static/css/components/user.css';

import {Link} from 'react-router-dom';
import profile from '../static/icons/profile.png';

function UserPage({ match }) {
    return (
        <div className="App">
            <div className="user-page">
                <section className="col">
                    <div className="left-panel">

                        <div className="user-options">

                            <div className="user-photo">
                                <img src={profile} alt="profile"/>
                            </div>
                            <div className="username">
                                <h3>Username</h3>
                            </div>

                            <div className="followers">
                                <h3>0 followers 0 following</h3>
                            </div>

                            <nav className="options">
                                <ul>
                                    <li><Link to="#">Edit Details</Link></li>
                                    <li><Link to="#">New Post</Link></li>
                                    <li><Link to="#">New Project</Link></li>
                                    <li><Link to="#">Settings</Link></li>
                                </ul>
                            </nav>
                        </div>  
                    </div>
                </section>

                <main className="col2">
                    <div className="main-panel">
                        <nav className="main-panel-header">
                            <ul>
                                <li className="pressed active"><Link to="#">Details</Link></li>
                                <li className="pressed"><Link to="#">Posts</Link></li>
                                <li className="pressed"><Link to="#">Projects</Link></li>
                            </ul>
                        </nav>

                        <section className="cnt details"></section>
                        <section className="cnt posts"></section>
                        <section className="cnt projects"></section>
                    </div>
                </main>
            </div>
        </div>
    )
}

export default UserPage;

let pressed = document.getElementsByClassName('pressed');

for ( let i = 0; i<pressed.length; i++) {
    pressed[i].onclick = function () {
        let current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace("active", " ");
        this.className += "active";
    }
}
