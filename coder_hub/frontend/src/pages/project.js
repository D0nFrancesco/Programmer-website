import $ from "jquery";
import React from 'react';


class Project extends React.Component {
    constructor(props) {
        super(props);
        this.project_id = props.match.params.projectid;

        this.state = {
            postTitle: 'Loading...',
            postText: 'Loading...',
            postAuthor: 'Loading...',
            postUpvotes: 0,
            postDownvotes: 0,
        };
    }

    render() {
        return (
            <div className="App">
                <div className="center">
                    <div className="card">
                        <div>
                            <h3>{ this.state.postTitle }</h3>
                            <span>{ this.state.postAuthor }</span>
                        </div>
                        <span>{ this.state.postText }</span>
                        <div className="post-bar">
                            <div>{ this.state.postUpvotes }</div>
                            <div>{ this.state.postDownvotes }</div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    componentDidMount() {
        // Get API info
        var component = this;

        // post data
        $.get(
            `http://localhost:8000/api/post/${ this.project_id }`
        ).done(function(data) {
            console.log(data);
            component.setState({
                postTitle: data.title,
                postText: data.text,
                postUpvotes: data.upvoted_by.len ? data.upvoted_by.len : 0,
                postDownvotes: data.downvoted_by.len ? data.downvoted_by.len : 0,
            });

            $.get(
                `http://localhost:8000/api/user/${ data.user }`
            ).done(function(data) {
                component.setState({
                    postAuthor: data.username
                });
            })
        });

        
    }
}

export default Project;
