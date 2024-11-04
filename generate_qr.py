import qrcode

def create_qr_code(url, filename="my_github_qr.png"):
    print(f"Generating QR code for {url}...")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code saved as {filename}.")

if __name__ == "__main__":
    import os
    url = os.getenv('QR_DATA_URL', 'https://github.com/HarshithaParupalli')
    create_qr_code(url)
