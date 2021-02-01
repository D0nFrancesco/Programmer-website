// CSS
import '../static/css/components/post.css'

// Images
import vote_icon from '../static/icons/arrow.svg';
import comment_icon from '../static/icons/comment.svg';
import report_icon from '../static/icons/flag.svg'


function Post({ title, content, poster_name, n_upvotes, n_comments}) {
    return (
        <div className="card post" style={{ width: "500px" }}>
                <div className="post-header">
                    <div className="post-information">
                    <h3>{title}</h3>
                    <div style={{ width: "10px" }}></div>
                    <p>-</p>
                    <div style={{ width: "10px" }}></div>
                    <span className="post-user">{  poster_name }</span>
                </div>
                <div>
                    <img src={ report_icon } alt="Report button"/>
                </div>
            </div>

            <div style={{ height: "10px" }}></div>

            <div className="post-content">
                <span>{content}</span>
            </div>

            <div style={{ height: "10px" }}></div>

            <div className="post-action-bar">
                <div className="votes">
                    <img className="icon" src={ vote_icon } alt="Upvote button"/>
                    <div style={{ width: "5px" }}></div>
                    <span>{ n_upvotes }</span>
                    <div style={{ width: "5px" }}></div>
                    <img className="icon" src={ vote_icon } style={{ rotate: "180deg" }} alt="Downvote button"/>
                </div>

                <div className="comments">
                    <span>{ n_comments }</span>
                    <div style={{ width: "10px" }}></div>
                    <img className="icon" src={ comment_icon } alt="Comments button"/>
                </div>
            </div>
        </div>
    )
}

export default Post;
