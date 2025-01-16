import google.generativeai as genai

def buat_pertanyaan(model_name, pertanyaan, history=None):
    """Membuat pertanyaan ke model Gemini dengan riwayat percakapan."""
    try:
        model = genai.GenerativeModel(model_name)
        if history:
            pertanyaan_dengan_history = "\n".join(history) + "\n" + pertanyaan
        else:
            pertanyaan_dengan_history = pertanyaan
        response = model.generate_content(pertanyaan_dengan_history)
        return response.text
    except Exception as e:
        # Warna ANSI
        red = "\033[31m"  # Merah
        blue = "\033[34m"  # Biru
        reset = "\033[0m"  # Reset warna

        # Mencetak pesan kesalahan dengan warna merah dan detail error dengan warna biru
        print(f"{red}Terjadi kesalahan di apikey / api key tidak valid:{reset}\n\t{blue}{e}{reset}")

        return None

def main():
    """Fungsi utama untuk menjalankan chatbot."""
    model_dipilih = "gemini-pro"  # Default model: gemini-pro
    history = []  # Inisialisasi riwayat percakapan

    # Logo AIMU dengan warna ungu
    purple = "\033[35m"  # Warna ungu
    reset = "\033[0m"  # Reset ke warna default
    aimu = f"""
{purple}
            ▄▀█ █ █▀▄▀█ █░█ ▀▄▀
            █▀█ █ █░▀░█ █▄█ █░█
        Selamat datang di Aimux Chatbot
{reset}
"""
    print(aimu)

    # Meminta API key setelah menampilkan pesan selamat datang
    api = input("Masukkan API key AI Gemini Anda: ")
    genai.configure(api_key=api)

    # Meminta input karakter AI di awal
    karakter_ai = input("Masukkan karakter AI yang Anda inginkan (misalnya: kucing, detektif, dll.): ")
    history.append(f"Kamu adalah seorang {karakter_ai}.")

    while True:
        print("\nModel yang digunakan: gemini-pro")  # Menampilkan model yang digunakan
        print("Ketik 'keluar' untuk mengakhiri.")

        pertanyaan = input("Anda: ")
        if pertanyaan.lower() == "keluar":
            break

        jawaban = buat_pertanyaan(model_dipilih, pertanyaan, history)

        if jawaban:
            # Warna ungu untuk jawaban AI
            purple = "\033[35m"  # Warna ungu
            reset = "\033[0m"  # Reset ke warna default
            print(f"{purple}Aimux : {jawaban}{reset}")
            history.append(f"Anda: {pertanyaan}")
            history.append(f"Aimux ({karakter_ai}): {jawaban}")

if __name__ == "__main__":
    main()
