

function Project({match}) {
    return (
        <div className="App">
            <div className="center">
                <div className="card">
                    <h3>Project page</h3>
                    <span>{ match.params.projectid }</span>
                </div>
            </div>
        </div>
    )
}

export default Project;
