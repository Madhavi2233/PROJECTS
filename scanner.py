import cv2

# Load QR image
img = cv2.imread("generated_qr/my_qr.png")

# Create detector
detector = cv2.QRCodeDetector()

# Detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# Print result
if data:
    print("Scanned Data:", data)
else:
    print("No QR code found")