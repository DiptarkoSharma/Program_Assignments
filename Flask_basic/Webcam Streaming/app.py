from flask import Flask,render_template,Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def frame_generator():
    #Read frames continuously from the camera   
    while True:
        #Read the camera frame
        success,frame = camera.read()
        print(f'Success Status is {success}')
        if not success:
            print('breaking off')
            break
        else:
            #Encode frame in the form of jpg
            ret,buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
        yield (b'--frame\r\n'
                   b'Content-Type:image/jpeg\r\n\r\n'+ frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(frame_generator(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ =='__main__':
    app.run(debug=True)



