import React from "react";
import ReactDOM from "react-dom";
import "@babel/polyfill";

const App = () => {
    return (
        <div>
            <h1>Index</h1>
        </div>
    );
};

var mountNode = document.getElementById("content");

ReactDOM.render(<App />, mountNode);

