from flask import Flask, request, jsonify,render_template,redirect,url_for
from pytube import YouTube

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/done.html')
def done_page():
    return render_template('done.html')

@app.route('/error.html')
def error_page():
    return render_template('error.html')

@app.route('/download', methods=['POST'])
def download_audio():
    data=request.get_json()
    url=data['url']      
    try:
        ytb=YouTube(url)   
        title=ytb.title 
        audio=ytb.streams.filter(only_audio=True).first()        
        audio.download(output_path='/Users/sharvaniadiga/Music/Downloaded',filename=title+'.mp3')       #change the output_path to the desired path.
        message = f"Download of '{title}' successful!"
    except Exception as e:
        message = f"Error occurred: {e}"
    return jsonify({'message':message})
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/redirect_to_index')
def redirect_to_index():
    return redirect(url_for('index'))
