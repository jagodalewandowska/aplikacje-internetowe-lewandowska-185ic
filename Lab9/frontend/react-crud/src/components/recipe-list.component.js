import React, { Component } from "react";
import RecipeDataService from "../services/recipe.service";
import { Link } from "react-router-dom";

export default class RecipesList extends Component {
  constructor(props) {
    super(props);
    this.onChangeSearchTitle = this.onChangeSearchTitle.bind(this);
    this.retrieveRecipes = this.retrieveRecipes.bind(this);
    this.refreshList = this.refreshList.bind(this);
    this.setActiveRecipe = this.setActiveRecipe.bind(this);
    this.removeAllRecipes = this.removeAllRecipes.bind(this);
    this.searchTitle = this.searchTitle.bind(this);

    this.state = {
      Recipes: [],
      currentRecipe: null,
      currentIndex: -1,
      searchTitle: ""
    };
  }

  componentDidMount() {
    this.retrieveRecipes();
  }

  onChangeSearchTitle(e) {
    const searchTitle = e.target.value;

    this.setState({
      searchTitle: searchTitle
    });
  }

  retrieveRecipes() {
    RecipeDataService.getAll()
      .then(response => {
        this.setState({
          Recipes: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  refreshList() {
    this.retrieveRecipes();
    this.setState({
      currentRecipe: null,
      currentIndex: -1
    });
  }

  setActiveRecipe(Recipe, index) {
    this.setState({
      currentRecipe: Recipe,
      currentIndex: index
    });
  }

  removeAllRecipes() {
    RecipeDataService.deleteAll()
      .then(response => {
        console.log(response.data);
        this.refreshList();
      })
      .catch(e => {
        console.log(e);
      });
  }

  searchTitle() {
    RecipeDataService.findByTitle(this.state.searchTitle)
      .then(response => {
        this.setState({
          Recipes: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  render() {
    const { searchTitle, Recipes, currentRecipe, currentIndex } = this.state;

    return (
      <div className="list row">
        <div className="col-md-8">
          <div className="input-group mb-3">
            <input
              type="text"
              className="form-control"
              placeholder="Type in the name of your recipe..."
              value={searchTitle}
              onChange={this.onChangeSearchTitle}
            />
            <div className="input-group-append">
              <button
                className="btn btn-warning"
                type="button"                
                onClick={this.searchTitle}
              >
                <b className="colourme">Search your recipe!</b>
              </button>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <h4 className="colourme">Recipes</h4>

          <ul className="list-group">
            {Recipes &&
              Recipes.map((Recipe, index) => (
                <li
                  className={
                    "list-group-item list-group-item-warning" +
                    (index === currentIndex ? "active" : "")
                  }
                  onClick={() => this.setActiveRecipe(Recipe, index)}
                  key={index}
                >
                  {Recipe.title}
                </li>
              ))}
          </ul>

          <button
            className="m-3 btn btn-sm btn-danger"
            onClick={this.removeAllRecipes}
          >
            Remove All
          </button>
        </div>
        <div className="col-md-6">
          {currentRecipe ? (
            <div className="colourme">
              <div>
                <label style={{color: '#FFEEBA'}}>
                  <strong>Przepis na </strong>
                </label>{" "}
                {currentRecipe.title}
              </div>
              <div className="colourme">
                <label style={{color: '#FFEEBA'}}>
                  Opis:
                </label>{" "}
                {currentRecipe.description}
              </div><br/>
              <div className="colourme">                
                <label style={{color: '#FFEEBA'}}>
                  Status:
                </label>{" "}
                {currentRecipe.published ? "Opublikowany" : "Oczekujący"}
              </div>

              <Link
                to={"/recipes/" + currentRecipe.id}
                className="badge badge-pill badge-warning"   
                style={{color: 'white'}}             
              >
                <h7>Edytuj status</h7>
              </Link>
            </div>
          ) : (
            <div>
              <br />
              <p className="colourme">Choose a recipe from the list, to see the details.</p>
            </div>
          )}
        </div>
      </div>
    );
  }
}