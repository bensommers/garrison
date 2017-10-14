import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work.js';

const myWork = [
  {
    'title': "HOME",
    'image': {
      'desc': "house",
      'src': "images/example1.png",
      'comment': "",
    }
  },
  {
    'title': "Pets",
    'image': {
      'desc': "Pets Description",
      'src': "images/example2.png",
      'comment': "",
    }
  },
  {
    'title': "Automobiles",
    'image': {
      'desc': "cars and shit",
      'src': "images/example3.png",
      'comment': "",
    }
  }
]

ReactDOM.render(<ExampleWork work={myWork} />, document.getElementById('example-work'));
