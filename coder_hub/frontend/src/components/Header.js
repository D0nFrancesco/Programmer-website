import { FaSearch, FaEnvelope, FaUser } from 'react-icons/fa';

const Header = () => {
    return (
        <nav className="nav">
            
            <div className="nav-container">
                {/* logo */}
                <div className="logo"><h1>Coder Hub</h1></div>    
                {/* search bar and menu */}
                <div className="search-menu">
                    {/* menu list */}
                    <ul className="menu">
                        <li>Home</li>
                        <li>Projects</li>
                        <li>Social</li>
                    </ul>
                    {/* search bar */}
                    <form action="" method="post">
                        <div className="search">
                            <input type="search" name="" id=""/>
                            {/* button with search icon */}
                            <button type="submit" className="btn-src"><FaSearch /></button>
                        </div>
                    </form>
                </div>
                {/* email and account */}
                <div className="mail-account">
                    {/* mail icon */}
                    <FaEnvelope id="mail" />
                    {/* account icon */}
                    <p>Account &nbsp;&nbsp;<FaUser /></p>
                </div>
            </div>
        </nav>
    )
}

export default Header
