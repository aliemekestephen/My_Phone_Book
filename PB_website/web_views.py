from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import User, Phone
from . import db
import json

web_views = Blueprint('web_views', __name__)


@web_views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    headings = ("No.", "Name", "Mobile no.", "Phone no.", "Birthdate", "Email", "Options")
    cons = Phone.query.filter_by(user_id=User.get_id(current_user))
    return render_template("pb_home.jinja2", user=current_user, headings=headings, cons=cons)


@web_views.route('/delete_contact', methods=['POST'])
def delete_contact():
    phone = json.loads(request.data)
    phoneId = phone['phoneId']
    phone = Phone.query.get(phoneId)
    if phone:
        if phone.user_id == current_user.id:
            db.session.delete(phone)
            db.session.commit()

    return jsonify({})
