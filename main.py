import qrcode

def generate_qr_code(link):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qr_code.png")
    print("QR code generated successfully!")

# Example usage
link = "https://www.friv.com/"
generate_qr_code(link)
