import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';

const socket = io('http://localhost:8000');

function takePicture() {
  socket.emit('take_picture');
}



function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [displayText, setDisplayText] = useState('Placeholder Text');
  const [displayTextUltrasonic, setDisplayTextUltrasonic] = useState('Placeholder Text');
  const [displayTextLight, setDisplayTextLight] = useState('Placeholder Text');
  const [displayTextHumidity, setDisplayTextHumidity] = useState('Placeholder Text');
  const [myInput, setMyInput] = useState("");

  function switchWatchMode() {
    console.log(myInput);
    if (myInput === "1" || myInput === "2") {
      socket.emit('watchmode', myInput);
    }
    else if (myInput === "") {
      socket.emit('watchmode', "none");
    }
    else {
      socket.emit('watchmode', myInput);
    }
  }


  useEffect(() => {

    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on("temp", (data) => {
      //console.log('Received from broker:', data);
      setDisplayText(`Temperature: ${data}`);
    });
    socket.on('ultrasonic', (data) => {
      //console.log('Received from broker:', data);
      setDisplayTextUltrasonic(`Distance: ${data}`);
    });
    socket.on('light', (data) => {
      //console.log('Received from broker:', data);
      setDisplayTextLight(`Light Level: ${data}`);
    });
    socket.on('humidity', (data) => {
      //console.log('Received from broker:', data);
      setDisplayTextHumidity(`Humidity: ${data}`);
    });

    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });

    return () => {
      socket.off('picture_taken');
      socket.off('temp');
    };
  }, []);

  return (
    <div className="app">
      <p>Write your code here!</p>
      <div>
        <button onClick={takePicture} className="ImageButton">Take Picture</button>
      </div>
      <div className="watch-mode-container">
        <label>
          Choose Watch Mode (1 for Watch, 2 for Data)
        </label>
        <div className="input-button-row">
          <input
            name="myInput"
            value={myInput}
            onChange={e => setMyInput(e.target.value)}
          />
          <button onClick={switchWatchMode} className="WatchButton">Submit watch mode</button>
        </div>
      </div>
      <div>
        <img
          src={`http://localhost:8000/image.jpg?t=${Date.now()}`}
          alt="Camera Image"
          className="CameraImage"
          style={{ width: "400px", height: "400px" }}
        />
      </div>
      <p>{displayText}<br></br>{displayTextUltrasonic}<br></br>{displayTextLight}<br></br>{displayTextHumidity}</p>
      <div>
        <audio autoplay controls>
          <source src={`http://localhost:8000/aiSpeech.mp3?t=${Date.now()}`} type="audio/mpeg" />
        </audio>
      </div>
    </div>
  );
}

export default App;
