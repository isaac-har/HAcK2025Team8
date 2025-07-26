import React, { useState, useEffect } from "react";
import io from 'socket.io-client';
import './App.css';
import placeholder from './placeholder.png';

const socket = io('http://localhost:8000');

function takePicture() {
  socket.emit('take_picture');
}

function App() {
  const [pictureStatus, setPictureStatus] = useState("");
  const [pictureName, setPictureName] = useState("");

  useEffect(() => {
    socket.on('connect', () => console.log('Connected:', socket.id));
    socket.on('picture_taken', data => {
      setPictureStatus(data.message);
      setTimeout(() => setPictureStatus(""), 3000); // Clear status after 3 seconds
    });
    socket.on('picture_name', picInput => {
      setPictureName(picInput);
      console.log(pictureName);

    });
    return () => {
      socket.off('picture_taken');
    };
  }, []);

  return (
    <div className="app">
      <p>Write your code here!</p>
      <div>
        <button onClick={takePicture} className="ImageButton">Take Picture</button>
      </div>
      <div>
        <img
          src={pictureName ? `http://localhost:8000/image.jpg?t=${Date.now()}` : placeholder}
          alt="Camera Image"
          className="CameraImage"
          style={{ width: "400px", height: "400px" }}
        />
      </div>
    </div>
  );
}

export default App;
