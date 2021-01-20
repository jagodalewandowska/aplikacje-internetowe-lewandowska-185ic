import React, { Component } from 'react';

class TodayIs extends Component {
  constructor() {
    super();
    var today = new Date(),
    date = today.getFullYear() + '/' + (today.getMonth() + 1) + '/' + today.getDate();

    this.state = {
      currentDate: date
    }
  }
  render() {
    return (
      <div>
        <h4> Today is {this.state.currentDate}. </h4>
      </div>
    );
  }
}

export default TodayIs;