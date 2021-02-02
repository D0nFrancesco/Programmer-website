

function UserPage({ match }) {
    return (
        <div className="App">
            <div className="center">
                <div className="card">
                    <h3>User page</h3>
                    <span>{ match.params.username }</span>
                </div>
            </div>
        </div>
    )
}

export default UserPage;
