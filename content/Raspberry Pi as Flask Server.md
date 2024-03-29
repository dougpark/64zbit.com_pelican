Title: Raspberry Pi as a Flask Server
Date: 2022-01-05 18:30
Category: Tech
Tags: programming, Pi
Summary: I created an Air Quality Index gadget made from a Raspberry Pi Zero W with a tiny OLED screen from Adafruit. It shows the AQI from my local PurpleAir sensor. I created a Flask web server on the Pi so I could remotely see the AQI and change the PurpleAir sensor ID.

I created an Air Quality Index gadget made from a Raspberry Pi Zero W with a tiny OLED screen from Adafruit. It shows the AQI from my local PurpleAir sensor. 

I created a Flask web server on the Pi so I could remotely see the AQI and change the PurpleAir sensor ID.



    :::python
    print("The triple-colon syntax will *not* show line numbers.")

    from flask import Flask, render_template, request, jsonify, make_response
    import os
    import logging
    import datastore
    import aqistore

    # DotMap is a dot-access dictionary subclass
    # https://pypi.org/project/dotmap/
    # https://github.com/drgrib/dotmap
    from dotmap import DotMap

    # logging configuration
    # debug, info, warning, error, critical
    logging.basicConfig(filename='./instance/aqi.log',
                        level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info('Started')
    logging.info('running server.py')

    # Example ajax code from
    # https://github.com/caseydunham/ajax-flask-demo

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'aqi.sqlite'),
        LOGGER=os.path.join(app.instance_path, 'aqi.log'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
        logging.info('server - created instance folder.')
    except OSError:
        pass

    # default sensor_id for PurpleAir sensor Forest Park
    sensor_id = 104402


    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/pi')
    def pi():
        return 'Raspberry Pie!'


    @app.route('/sensor')
    def sensor_index():
        return render_template('sensor.html')


    @app.route('/aqi')
    def aqi_index():
        resp = make_response(render_template('aqi.html'))
        resp.set_cookie('aqi', 'aqi')
        return resp


    @app.route('/api/sensor', methods=['GET', 'POST'])
    def get_sensor_post():
        logging.info('**************** starting sensor ')
        # logging.info('request user_agent: ', request.)
        out = get_sensor_proc()
        r = out.toDict()
        return jsonify(result=r, status=200)


    def get_sensor_proc():
        error = None
        out = DotMap()
        sensor_id = 0
        try:
            sensor_id = datastore.get_sensor_id()
        except Exception as e:
            error = e
            logging.warning(e)
        out.sensor_id = sensor_id
        out.error = error
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
        logging.info('get_sensor_proc - sensor_id from db.', out.toDict())
        return out


    @app.route('/api/aqi', methods=['GET', 'POST'])
    def aqi_post():
        logging.info('**************** starting aqi ')
        # logging.info('request user_agent: ', request.)
        out = aqi_proc()
        r = out.toDict()
        return jsonify(result=r, status=200)


    def aqi_proc():
        error = None
        aqi = 0
        aqiColor = 0
        try:
            out = aqistore.purpleAir()
        except Exception as e:
            error = e
            logging.warning(e)
        out.error = error
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
        logging.info('aqi_proc - data from purpleAir.', out.toDict())
        return out


    @app.route('/api/sensor_post', methods=['POST'])
    def sensor_post():
        json = request.get_json()
        msg = DotMap(json)
        out = sensor_proc(msg)
        r = out.toDict()
        return jsonify(result=r, status=200)


    def sensor_proc(msg):
        sensor_id = msg.sensor_id
        logging.info('server - updating db sensor_id: ' + str(sensor_id))
        error = None

        if not sensor_id:
            error = 'Sensor_id is required.'
            logging.warning(error)

        if error is None:
            error = datastore.set_sensor_id(sensor_id)
        out = DotMap()
        out.sensor_id = sensor_id
        out.error = error
        return out


    @app.route('/api/say_name', methods=['POST'])
    def say_name_post():
        json = request.get_json()
        msg = DotMap(json)
        out = say_name_proc(msg)
        r = out.toDict()
        return jsonify(result=r, status=200)

    # process say_name message


    def say_name_proc(msg):
        datastore.get_db()
        first_name = msg.first_name
        last_name = msg.last_name
        day_week = msg.day_week

        out = DotMap()
        out.first_name = first_name
        out.last_name = last_name
        out.day_week = day_week
        datastore.close_db()
        return out


    @app.route('/init')
    def init():
        datastore.init_db()
        return 'Database initialized'

    # dynamic route


    @app.route('/<name>')
    def print_name(name):
        return 'Hi, {}'.format(name)


    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

