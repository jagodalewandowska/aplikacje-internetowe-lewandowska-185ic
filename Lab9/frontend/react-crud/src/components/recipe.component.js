import React, { Component } from "react";
import RecipeDataService from "../services/recipe.service";

export default class Recipe extends Component {
  constructor(props) {
    super(props);
    this.onChangeTitle = this.onChangeTitle.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.getRecipe = this.getRecipe.bind(this);
    this.updatePublished = this.updatePublished.bind(this);
    this.updateRecipe = this.updateRecipe.bind(this);
    this.deleteRecipe = this.deleteRecipe.bind(this);

    this.state = {
      currentRecipe: {
        id: null,
        title: "",
        description: "",
        published: false
      },
      message: ""
    };
  }

  componentDidMount() {
    this.getRecipe(this.props.match.params.id);
  }

  onChangeTitle(e) {
    const title = e.target.value;

    this.setState(function(prevState) {
      return {
        currentRecipe: {
          ...prevState.currentRecipe,
          title: title
        }
      };
    });
  }

  onChangeDescription(e) {
    const description = e.target.value;
    
    this.setState(prevState => ({
      currentRecipe: {
        ...prevState.currentRecipe,
        description: description
      }
    }));
  }

  getRecipe(id) {
    RecipeDataService.get(id)
      .then(response => {
        this.setState({
          currentRecipe: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  updatePublished(status) {
    var data = {
      id: this.state.currentRecipe.id,
      title: this.state.currentRecipe.title,
      description: this.state.currentRecipe.description,
      published: status
    };

    RecipeDataService.update(this.state.currentRecipe.id, data)
      .then(response => {
        this.setState(prevState => ({
          currentRecipe: {
            ...prevState.currentRecipe,
            published: status
          }
        }));
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  updateRecipe() {
    RecipeDataService.update(
      this.state.currentRecipe.id,
      this.state.currentRecipe
    )
      .then(response => {
        console.log(response.data);
        this.setState({
          message: "The Recipe was updated successfully!"
        });
      })
      .catch(e => {
        console.log(e);
      });
  }

  deleteRecipe() {    
    RecipeDataService.delete(this.state.currentRecipe.id)
      .then(response => {
        console.log(response.data);
        this.props.history.push('/recipes')
      })
      .catch(e => {
        console.log(e);
      });
  }

  render() {
    const { currentRecipe } = this.state;

    return (
      <div className="colourme">
        {currentRecipe ? (
          <div className="edit-form">
            <h4>Przepis</h4>
            <form>
              <div className="form-group">
                <label htmlFor="title">Title</label>
                <input
                  type="text"
                  className="form-control"
                  id="title"
                  value={currentRecipe.title}
                  onChange={this.onChangeTitle}
                />
              </div>
              <div className="form-group">
                <label htmlFor="description">Przygotowanie</label>
                <input
                  type="text"
                  className="form-control"
                  id="description"
                  value={currentRecipe.description}
                  onChange={this.onChangeDescription}
                />
              </div>

              <div className="form-group">
                <label>
                  <strong>Status:</strong>
                </label>
                {currentRecipe.published ? "Opublikowany" : "Oczekujący"}
              </div>
            </form>

            {currentRecipe.published ? (
              <button
                className="badge badge-primary mr-2"
                onClick={() => this.updatePublished(false)}
              >
                UnPublish
              </button>
            ) : (
              <button
                className="badge badge-primary mr-2"
                onClick={() => this.updatePublished(true)}
              >
                Publish
              </button>
            )}

            <button
              className="badge badge-danger mr-2"
              onClick={this.deleteRecipe}
            >
              Delete
            </button>

            <button
              type="submit"
              className="badge badge-success"
              onClick={this.updateRecipe}
            >
              Update
            </button>
            <p>{this.state.message}</p>
          </div>
        ) : (
          <div>
            <br />
            <p>Please click on a Recipe...</p>
          </div>
        )}
      </div>
    );
  }
}