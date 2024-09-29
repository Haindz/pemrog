from PIL import Image

# Fungsi untuk menyembunyikan pesan ke dalam gambar
def encode_message(image_path, message, output_path):
    # Buka gambar
    img = Image.open(image_path)
    encoded_img = img.copy()
    width, height = img.size
    pixels = encoded_img.load()

    # Konversi pesan ke biner
    message += chr(0)  # Menambahkan karakter akhir pesan (Null terminator)
    binary_message = ''.join([format(ord(i), "08b") for i in message])

    # Pastikan pesan tidak terlalu panjang
    if len(binary_message) > width * height * 3:
        raise ValueError("Pesan terlalu panjang untuk disembunyikan dalam gambar ini.")

    # Menyembunyikan pesan dalam pixel
    idx = 0
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])

            # Jika gambar memiliki channel alpha (RGBA), abaikan channel alpha
            for i in range(3):  # Hanya edit channel RGB (bukan alpha)
                if idx < len(binary_message):
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[idx])
                    idx += 1
            pixels[x, y] = tuple(pixel)

    # Simpan gambar hasil encode
    encoded_img.save(output_path)
    print("Pesan berhasil disembunyikan ke dalam gambar.")


# Contoh penggunaan
input_image = 'C:/Users/HAFIDZ/OneDrive/Documents/Kuliah/Aljabar Linier/coba.png'  # Path ke gambar input
output_image = 'C:/Users/HAFIDZ/OneDrive/Documents/Kuliah/Aljabar Linier/anayycoba.png'  # Path ke gambar hasil encode
pesan = "cihuyyyyyyy anjayyyyy"  # Pesan yang akan disembunyikan

# Sembunyikan pesan
encode_message(input_image, pesan, output_image)
