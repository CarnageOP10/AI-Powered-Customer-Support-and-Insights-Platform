from custom import app
from flask import render_template, redirect, url_for, flash, request
from custom.forms import RaiseForm
from custom.models import Query
from custom import db
from custom.llm import query_classifier

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/success')
def success_page():
    return render_template('thanku.html')

@app.route('/form', methods=['GET', 'POST'])
def raiseAlert_form():
    form = RaiseForm()
    if form.validate_on_submit():

        query1 = form.complain.data
        product_info = query_classifier.invoke({"query": query1})

        query = Query(
            name=form.name.data,
            mobile_number=form.mo_number.data,
            state_name=form.state_name.data.upper(),
            city_name=form.city_name.data.lower(),
            pincode=form.pincode.data,
            description=product_info.product_desc,
            product_type = product_info.product_type,
            severity = product_info.severity

        )

        db.session.add(query)
        db.session.commit()
        flash(f"Alert Raised successfully!", category='success')
        return redirect(url_for('success_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('form.html', form=form)

