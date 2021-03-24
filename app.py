# Import libraries
from flask import Flask, render_template, url_for

app = Flask(__name__)


# @app.route('/')
# def home():
#     return render_template('plot.html')

@app.route('/')
def home():
    
    from bokeh.embed import components
    from bokeh.resources import CDN

   
    # Plot 1
    from plot import plot1
    plot_1 = plot1()
    
    # Plot 2
    from plot import plot2
    plot_2 = plot2()
   

    # Javascript and Div Tags for the 2 plots
    script1, div1 = components(plot_1)
    script2, div2 = components(plot_2)
    
    # (script1, (div1, div2)) = components((plot_1, plot_2))
    
    
    return render_template('plot.html', script1=script1, script2=script2, div1=div1, div2=div2)


if __name__ == '__main__':
    app.run(debug=True)