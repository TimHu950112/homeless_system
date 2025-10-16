from flask import Blueprint, render_template, send_file, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from app.database import db
import qrcode
from io import BytesIO
import base64
import json
from datetime import datetime

bp = Blueprint('food', __name__, url_prefix='/food')

@bp.route('/')
def index():
    providers = db.find('food_providers', is_active=True)
    return render_template('food/index.html', providers=providers)

@bp.route('/my-vouchers')
@login_required
def my_vouchers():
    vouchers = db.find('meal_vouchers', user_id=current_user.id)

    # Generate QR codes for each voucher
    for voucher in vouchers:
        if not voucher.get('is_used'):
            # Create QR code data
            qr_data = {
                'voucher_id': voucher.get('id'),
                'user_id': current_user.id,
                'meal_type': voucher.get('meal_type'),
                'issued_date': voucher.get('issued_date'),
                'expiry_date': voucher.get('expiry_date')
            }

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(json.dumps(qr_data))
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Convert to base64
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            voucher['qr_code'] = img_str

    return render_template('food/my_vouchers.html', vouchers=vouchers)

@bp.route('/voucher/<int:voucher_id>/qrcode')
@login_required
def voucher_qrcode(voucher_id):
    """生成單張餐券的 QR Code 圖片"""
    voucher = db.get_by_id('meal_vouchers', voucher_id)

    if not voucher or voucher.get('user_id') != current_user.id:
        flash('找不到該餐券。', 'danger')
        return redirect(url_for('food.my_vouchers'))

    # Create QR code data
    qr_data = {
        'voucher_id': voucher.get('id'),
        'user_id': current_user.id,
        'meal_type': voucher.get('meal_type'),
        'issued_date': voucher.get('issued_date'),
        'expiry_date': voucher.get('expiry_date')
    }

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(qr_data))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Return image
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)

    return send_file(buffered, mimetype='image/png')

@bp.route('/verify-voucher', methods=['GET', 'POST'])
@login_required
def verify_voucher():
    """驗證餐券（供餐廳人員使用）"""
    if request.method == 'POST':
        qr_data = request.form.get('qr_data')

        try:
            data = json.loads(qr_data)
            voucher_id = data.get('voucher_id')

            voucher = db.get_by_id('meal_vouchers', voucher_id)

            if not voucher:
                return jsonify({'success': False, 'message': '餐券不存在'})

            if voucher.get('is_used'):
                return jsonify({
                    'success': False,
                    'message': '此餐券已被使用',
                    'used_date': voucher.get('used_date')
                })

            # Check expiry
            if voucher.get('expiry_date'):
                expiry = datetime.fromisoformat(voucher.get('expiry_date'))
                if datetime.now() > expiry:
                    return jsonify({'success': False, 'message': '餐券已過期'})

            # Mark as used
            db.update('meal_vouchers', voucher_id, {
                'is_used': True,
                'used_date': datetime.now().isoformat(),
                'provider_name': request.form.get('provider_name', '未記錄')
            })

            return jsonify({
                'success': True,
                'message': '餐券驗證成功！',
                'voucher': {
                    'id': voucher.get('id'),
                    'meal_type': voucher.get('meal_type'),
                    'user_id': voucher.get('user_id')
                }
            })

        except Exception as e:
            return jsonify({'success': False, 'message': f'驗證失敗：{str(e)}'})

    return render_template('food/verify_voucher.html')
