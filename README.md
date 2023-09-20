# YouTube Audio Extraction Project

## Description

This project allows users to extract audio from YouTube videos by providing the URL of the video. It consists of a front-end built using HTML, CSS, and JavaScript, and a back-end implemented in Python using the Flask framework. The back-end uses the `pytube` library to download the audio from the YouTube video.

## Features

- **Audio Extraction:** Users can enter the URL of any YouTube video and extract the audio from it.
- **Front-end UI:** The front-end provides a simple and user-friendly interface to input the URL.
- **Back-end Processing:** The back-end server processes the URL and downloads the audio using the `pytube` library.
- **Feedback to User:** The user is provided with a message indicating whether the download was successful or if any errors occurred during the process.

## Project Structure
- `audio.py`: Flask back-end implementation
- `templates/`
  - `index.html`: Front-end HTML file for user input
  - `done.html`: Front-end HTML file for successful download
  - `error.html`: Front-end HTML file for error message
- `static/`
  - `design.css`: CSS styling for the front-end

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies (Python, Flask, pytube).
3. In the file "audio.py", add the path where you want the audio file to be downloaded.
4. Run the program with the command
       python3 audio.py
5. Access the application in your web browser at `http://localhost:5000`.
6. Enter the URL of the YouTube video in the search box and click the "Download" button.
7. After the download is complete, you will be redirected to the "Thank you for downloading" page with an option to download again.
