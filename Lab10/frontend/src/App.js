import React, { Component } from "react";
import Modal from "./components/Modal";
import Header from './components/Header';
import TodayIs from "./components/TodayIs";
import './App.css'
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewFinished: false,
      activeItem: {
        title: "",
        description: "",
        notes: "",
        finished: false,
        date: ""
      },
      recordsList: [],      
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  /* Wywoływana za każdym razem, kiedy zapytanie API jest wykonane
  Aktualizuje wyświetlanie listy do tych ostatnio dodanych */
  refreshList = () => {
    axios
      .get("http://localhost:8000/api/records/")
      .then(res => this.setState({ recordsList: res.data }))
      .catch(err => console.log(err));
  };

  displayFinished = status => {
    if (status) {
      return this.setState({ viewFinished: true });
    }
    return this.setState({ viewFinished: false });
  }; 

  renderTabList = () => {
    return (
      <div className="">
        <button onClick={() => this.displayFinished(true)}
          className={this.state.viewFinished ? "active" : ""}
          type="button" 
          // eslint-disable-next-line
          className="btn btn-primary btn-lg btn-block btn-secondary">
          Completed tasks
        </button>
        <br></br>
        <button onClick={() => this.displayFinished(false)}
          className={this.state.viewFinished ? "" : "active"}
          type="button" 
          // eslint-disable-next-line
          className="btn btn-primary btn-lg btn-block btn-warning">
          Incompleted tasks
        </button>
      </div>
    );
  };  
  
  outDated = item => {
    const now = new Date();
    now.setHours(0,0,0,0);
    const then = new Date(item.date);
    then.setHours(0,0,0,0);
    if (now.getTime() <= then.getTime()) {
      return false;
    } else {
      return true;
    }
  };

  renderItems = () => {
    const { viewFinished } = this.state;
    const newItems = this.state.recordsList.filter(
      item => item.finished === viewFinished
    );   

    return newItems.map(item => (
      <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
        <span className={`${this.state.viewFinished ? "completed-todo" : ""}`}>
          <h3>{item.title}</h3>
          <p style={{color: 'gray'}}>{item.description}</p>
          {this.outDated(item) ? <b style={{color: 'red'}}>It's past the deadline: {item.date}</b>
            : <b style={{color: 'green'}}>Deadline: {item.date}</b>}
        </span>  
        <span>
          <button onClick={() => this.editItem(item)} className="btn btn-info"> Edit </button>
          <button onClick={() => this.handleDelete(item)} className="btn btn-danger"> Delete </button>
        </span>
      </li>
    ));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  /* Zarządza operacjami stworzenia i aktualizacji, jeśli 
  obiekt jest przekazany jako parametr bez id to takie id
  kreuje dla tego obiektu */
  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(`http://localhost:8000/api/records/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/records/", item)
      .then(res => this.refreshList());
  };
  handleDelete = item => {
    axios
      .delete(`http://localhost:8000/api/records/${item.id}`)
      .then(res => this.refreshList());
  };

  createItem = () => {
    const item = { title: "", description: "", notes: "", finished: false, date: ""};
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  }; 

  render() {
    return (
      <div>
        <nav className="navbar navbar-expand-sm bg-info navbar-dark">      
          <div className="navbar-nav">            
            <a className="nav-link active" htef="/">Scheduler</a>
            <a className="nav-link" href="https://github.com/jagodalewandowska">Github</a>
          </div>
          <ul className="nav navbar-nav ml-auto" style = {{color: 'white'}}>
            Laboratorium 10
          </ul>
        </nav>
        <div>
          <Header />
            <div className="card">
                <div className="card-header">
                  <TodayIs /> 
                </div>             
              <div className="card-body">
                <div className="row">
                  <div className="col-4">
                    {this.renderTabList()}
                    <br></br>
                    <button onClick={this.createItem} type="button" className="btn btn-primary btn-lg btn-block btn-info">
                      Add task
                    </button>
                  </div>
                  <div className="col-8">                    
                    <ul className="list-group list-group-flush">
                    {this.renderItems()}
                    </ul>
                  </div>
                </div>
              </div> 
            {this.state.modal ? (
              <Modal
                activeItem={this.state.activeItem}
                toggle={this.toggle}
                onSave={this.handleSubmit}
              />
            ) : null} 
          </div>
        </div> 
      </div>
    );
  }
}
export default App;