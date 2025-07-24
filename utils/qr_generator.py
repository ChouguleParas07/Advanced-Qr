# utils/qr_generator.py - QR Code Generation Logic

import qrcode
from PIL import Image
import os
import uuid
from datetime import datetime

class QRGenerator:
    def __init__(self, qr_dir='static/qr_codes'):
        self.qr_dir = qr_dir
        os.makedirs(qr_dir, exist_ok=True)
    
    def generate_qr_code(self, data, size=10, border=4):
        """Generate QR code and save as PNG file"""
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=border,
        )
        
        # Add data and optimize
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"qr_{timestamp}_{unique_id}.png"
        filepath = os.path.join(self.qr_dir, filename)
        
        # Save image
        qr_image.save(filepath)
        
        return filename
    
    def generate_custom_qr(self, data, fill_color="black", back_color="white", size=10):
        """Generate QR code with custom colors"""
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=size,
            border=4,
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        filename = f"custom_qr_{timestamp}_{unique_id}.png"
        filepath = os.path.join(self.qr_dir, filename)
        
        qr_image.save(filepath)
        return filename
