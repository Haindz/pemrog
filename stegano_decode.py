from PIL import Image

# Fungsi untuk mengambil pesan dari gambar
def decode_message(image_path):
    # Buka gambar
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Ambil biner dari gambar
    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            for i in range(3):  # Hanya ambil channel RGB (bukan alpha)
                binary_message += str(pixel[i] & 1)

    # Konversi biner menjadi string
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''.join([chr(int(char, 2)) for char in chars])

    # Berhenti saat bertemu Null terminator
    return message.split(chr(0))[0]

# Contoh penggunaan
input_image = 'C:/Users/HAFIDZ/OneDrive/Documents/Kuliah/Aljabar Linier/coba.png'  # Path ke gambar input
output_image = 'C:/Users/HAFIDZ/OneDrive/Documents/Kuliah/Aljabar Linier/anayycoba.png'  # Path ke gambar hasil encode
pesan = "cihuyyyyyyy anjayyyyy"  # Pesan yang akan disembunyikan


# Ambil pesan dari gambar
decoded_message = decode_message(output_image)
print("Pesan tersembunyi:", decoded_message)
