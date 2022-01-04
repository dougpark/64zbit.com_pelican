Title: Tablet Review
Date: 2021-12-21 11:36
Category: Tech
Tags: programming, tablets

Following **is** a review of my favorite tablet. Oh Yea!

<!-- ![alt text]({static}images/image-1.png "image Title") -->
<img src="{static}images/image-1.png" alt="alt text" title="image Title" width="50%"/>

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


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget mauris pharetra et ultrices. Mauris nunc congue nisi vitae suscipit tellus. Leo integer malesuada nunc vel risus commodo viverra. Enim tortor at auctor urna nunc id cursus. Urna et pharetra pharetra massa massa. Sit amet mauris commodo quis imperdiet. Tempus urna et pharetra pharetra massa massa ultricies mi. Tempor id eu nisl nunc mi ipsum faucibus. Purus faucibus ornare suspendisse sed. Eget est lorem ipsum dolor sit amet consectetur. Scelerisque fermentum dui faucibus in ornare. Morbi tincidunt ornare massa eget egestas purus viverra accumsan. Et molestie ac feugiat sed lectus vestibulum. Pretium vulputate sapien nec sagittis. Porttitor leo a diam sollicitudin tempor. Dapibus ultrices in iaculis nunc.

Habitant morbi tristique senectus et netus et malesuada fames. Libero enim sed faucibus turpis in eu mi. Commodo elit at imperdiet dui accumsan sit amet. Tempor orci eu lobortis elementum. Quam lacus suspendisse faucibus interdum. Volutpat commodo sed egestas egestas. Sollicitudin nibh sit amet commodo nulla facilisi. Erat pellentesque adipiscing commodo elit at. Et tortor at risus viverra adipiscing at in tellus integer. Pulvinar elementum integer enim neque volutpat ac. Tempor id eu nisl nunc mi ipsum faucibus vitae. Tortor condimentum lacinia quis vel eros donec ac odio. Suspendisse ultrices gravida dictum fusce ut placerat orci.

Laoreet suspendisse interdum consectetur libero id. Faucibus vitae aliquet nec ullamcorper. Egestas diam in arcu cursus euismod quis viverra nibh cras. Amet consectetur adipiscing elit duis tristique sollicitudin nibh. Est sit amet facilisis magna etiam tempor orci eu lobortis. Sagittis eu volutpat odio facilisis mauris sit amet. Vestibulum sed arcu non odio euismod lacinia. Quis eleifend quam adipiscing vitae proin sagittis. Purus non enim praesent elementum facilisis. Justo eget magna fermentum iaculis. Adipiscing enim eu turpis egestas pretium aenean pharetra magna ac. Morbi tincidunt ornare massa eget egestas purus. Blandit cursus risus at ultrices mi.

Rutrum tellus pellentesque eu tincidunt tortor. Arcu cursus euismod quis viverra nibh cras pulvinar mattis nunc. Nisi vitae suscipit tellus mauris a diam. Aliquam vestibulum morbi blandit cursus risus at. Laoreet id donec ultrices tincidunt. Lorem donec massa sapien faucibus et molestie ac feugiat. Non odio euismod lacinia at quis risus sed vulputate. Vitae congue mauris rhoncus aenean vel elit. Eget mauris pharetra et ultrices neque ornare aenean euismod. Adipiscing enim eu turpis egestas pretium. Et tortor at risus viverra adipiscing at. In pellentesque massa placerat duis ultricies lacus sed turpis tincidunt. Vitae aliquet nec ullamcorper sit amet risus nullam eget. Scelerisque in dictum non consectetur a erat nam at lectus. Amet massa vitae tortor condimentum. Scelerisque in dictum non consectetur. Sapien eget mi proin sed. Tristique senectus et netus et malesuada fames. Morbi quis commodo odio aenean sed adipiscing diam donec.

Netus et malesuada fames ac turpis egestas sed tempus. Diam phasellus vestibulum lorem sed risus ultricies tristique nulla. Amet aliquam id diam maecenas ultricies mi eget mauris pharetra. Arcu bibendum at varius vel pharetra. In mollis nunc sed id semper. Non curabitur gravida arcu ac tortor dignissim convallis aenean et. At augue eget arcu dictum varius duis at. Velit dignissim sodales ut eu sem integer vitae justo. Amet est placerat in egestas erat imperdiet sed euismod nisi. Malesuada pellentesque elit eget gravida cum. Augue interdum velit euismod in pellentesque massa placerat. Eget magna fermentum iaculis eu non diam phasellus vestibulum. Integer vitae justo eget magna fermentum iaculis eu non diam. Tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius. Mattis aliquam faucibus purus in massa tempor nec feugiat. Viverra ipsum nunc aliquet bibendum enim facilisis. Ac ut consequat semper viverra nam libero justo laoreet sit. Nulla aliquet enim tortor at auctor. Sem integer vitae justo eget magna fermentum iaculis eu non.