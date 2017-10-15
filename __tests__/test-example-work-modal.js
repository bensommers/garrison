import React from 'react';
import { configure, shallow } from 'enzyme';
import ExampleWorkModal from '../js/example-work-modal';
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });

const myExample = {
  'title': "HOME",
  'href': "https://example.com",
  'desc':"bullshit bullshit bullshit",
  'image': {
    'desc': "example img",
    'src': "images/example1.png",
    'comment': ""
  }
};

describe("ExampleWOrkModal component", () =>{
  let component = shallow(<ExampleWorkModal example={myExample}
    open={false}/>);
  let openComponent = shallow(<ExampleWorkModal example={myExample}
    open={true}/>)

  let anchors = component.find("a");

  it ("Shound contain a single 'a' element", () => {
    expect(anchors.length).toEqual(1);
  });

  it("should link to our project", () => {
    expect(anchors.getElement().props.href).toEqual(myExample.href);
  });

  it("Should have the modal class set correctly", () => {
    expect(component.find(".background--skyBlue").hasClass("modal--closed")).toBe(true);
    expect(openComponent.find(".background--skyBlue").hasClass("modal--open")).toBe(true);
  })
});
