import React, { Component } from "react";
import PropTypes from "prop-types";

class Form extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired
  };

  state = {
    art_title: "",
    art_description: "",
    art_completion_date: "",
    medium: "",
    art_image: "",
    file_type: "",
    created_at: "",
    artist: ""
  };

  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

   handleSubmit = e => {
    e.preventDefault();
    const {art_title, art_description, art_completion_date, medium, art_image, file_type, created_at, artist} = this.state;
    const art = {art_title, art_description, art_completion_date, medium, art_image, file_type, created_at, artist};
    const conf = {
      method: "post",
      body: JSON.stringify(art),
      headers: new Headers({ "Content-Type": "application/json", "Authorization": "JWT YOUR_TOKEN_HERE",})
    };
    fetch(this.props.endpoint, conf).then(response => console.log(response));
  };

  render() {
    const {art_title, art_description, art_completion_date, medium, art_image, file_type, created_at, artist} = this.state;
    return (
      <div className="column">
        <form onSubmit={this.handleSubmit} method="post">
          <div className="field">
            <label className="label">art_title</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="art_title"
                onChange={this.handleChange}
                value={art_title}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">art_description</label>
            <div className="control">
              <textarea
                className="textarea"
                type="text"
                name="art_description"
                onChange={this.handleChange}
                value={art_description}
                required
              />
            </div>
          </div>
          <div className="field">
            <label className="label">art_completion_date</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="art_completion_date"
                onChange={this.handleChange}
                value={art_completion_date}
                required
              />
            </div>
          </div>
           <div className="field">
            <label className="label">medium</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="medium"
                onChange={this.handleChange}
                value={medium}
                required
              />
            </div>
          </div>
           <div className="field">
            <label className="label">art_image</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="art_image"
                onChange={this.handleChange}
                value={art_image}
                required
              />
            </div>
          </div>
           <div className="field">
            <label className="label">file_type</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="file_type"
                onChange={this.handleChange}
                value={file_type}
                required
              />
            </div>
          </div>
           <div className="field">
            <label className="label">created_at</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="created_at"
                onChange={this.handleChange}
                value={created_at}
                required
              />
            </div>
          </div>
           <div className="field">
            <label className="label">artist</label>
            <div className="control">
              <input
                className="input"
                type="text"
                name="artist"
                onChange={this.handleChange}
                value={artist}
                required
              />
            </div>
          </div>
          <div className="control">
            <button type="submit" className="button is-info">
              Add art to portfolio!
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default Form;