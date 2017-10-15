import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work.js';

const myWork = [
  {
    'title': "HOME",
    'href': "https://example.com",
    'desc':"Protect your house with state of the art GarrisonHomeDefense, don't be a doorknob!",
    'image': {
      'desc': "example img",
      'src': "images/example1.png",
      'comment': "",
    }
  },
  {
    'title': "Pets",
    'href': "https://example.com",
    'desc':"Protect your pets with the power of GarrisonPaws, order right meow!",
    'image': {
      'desc': "Pets Description",
      'src': "images/example2.png",
      'comment': "",
    }
  },
  {
    'title': "Automobiles",
    'href': "https://example.com",
    'desc':"Protect your autos with GarrisonAutoShield, it's wheely great!",
    'image': {
      'desc': "cars and shit",
      'src': "images/example3.png",
      'comment': "",
    }
  }
]

ReactDOM.render(<ExampleWork work={myWork} />, document.getElementById('example-work'));
