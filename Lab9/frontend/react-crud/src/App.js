import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Switch, Route, Link } from "react-router-dom";

import AddRecipe from "./components/add-recipe.component";
import Recipe from "./components/recipe.component";
import RecipeList from "./components/recipe-list.component";
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-expand navbar-dark bg-dark">
          <a href="/recipes" className="navbar-brand">
            RecipeBook
          </a>
          <div className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link to={"/recipes"} className="nav-link">
                Recipes
              </Link>
            </li>
            <li className="nav-item">
              <Link to={"/add"} className="nav-link">
                Add
              </Link>
            </li>
          </div>
        </nav>

        <div className="container mt-3">
          <Switch>
            <Route exact path={["/", "/recipes"]} component={RecipeList} />
            <Route exact path="/add" component={AddRecipe} />
            <Route path="/recipes/:id" component={Recipe} />
          </Switch>
        </div>
      </div>
    );
  }
}

export default App;