import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import base64
from flask import Flask, render_template, request
import io
from astropy.coordinates import SkyCoord
import astropy.units as u




app = Flask(__name__)



# Load the trained model
model = pickle.load(open('model/old.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

        
@app.route('/predict')
def test():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data1 = request.form['u']
        data2 = request.form['b']
        data3 = request.form['v']
        data4 = request.form['r']
        data5 = request.form['i']
        data6 = request.form['j']
        data7 = request.form['h']
        data8 = request.form['k']
        data9 = request.form['Vr']
        x = request.form['dec']
        y = request.form['ra']
    
        arr =np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9,x,y]])
        pred = model.predict(arr)

        image_path = 'static/img/plot.jpg'
        image = mpimg.imread(image_path)



        ra = float(request.form['ra']) * u.deg
        dec = float(request.form['dec']) * u.deg
        sky_coords = SkyCoord(ra, dec)



        fig, ax = plt.subplots(figsize=(8, 6))
        height, width, _ = image.shape
        ax.imshow(image, origin='upper', extent=[0, width, 0, height]) 

        ax.scatter(sky_coords.dec.deg, sky_coords.ra.deg, marker='o', color='red')

        fig.patch.set_facecolor('black')

        ax.tick_params(axis='x',colors='white')
        ax.tick_params(axis='y',colors='white')
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.yaxis.label.set_color('white')
        ax.xaxis.label.set_color('white')
        

        
        xlabel = ax.set_xlabel('Right Ascension (deg)')
        xlabel.set_color('white')
        xlabel
        ylabel = ax.set_ylabel('Declination (deg)')
        ylabel.set_color('white')
        ylabel
        title = ax.set_title('Sky Coordinate')
        title.set_color('white')
        title  
        ax.set_ylim([0,1800])

    
        # Save the plot to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Convert the plot to a base64-encoded string
        plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return render_template('plot.html', data=pred, plot_data=plot_data)
    else :
        return render_template('main.html')


if __name__ == '__main__':
    app.run()
    app.debug(True)
