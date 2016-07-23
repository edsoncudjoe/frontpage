from flask import render_template

from . import work


@work.route('/quicksearch')
def cdvqs():
    return render_template('cdv-qs.html')


@work.route('/cleanium')
def cleanium():
    return render_template('cleanium.html')


@work.route('/fbahunt')
def fbahunt():
    return render_template('fbahunt.html')


@work.route('/y2m')
def y2m():
    return render_template('y2m.html')



