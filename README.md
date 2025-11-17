# SudokuMultiAgen

Sebuah proyek sederhana yang membangun, memecahkan, memverifikasi, dan memvisualisasikan puzzle Sudoku menggunakan sistem multi-agen dengan Python dan AutoGen.

Proyek ini mendemonstrasikan kolaborasi tim agen AI khusus untuk menyelesaikan tugas multi-langkah, di mana mereka menulis dan mengeksekusi kode Python.

## Tim Agen

Sistem ini memiliki 5 agen yang dikelola oleh GroupChatManager (Manajer Proyek):

1. UserProxyAgent (user)

- Peran: Pelaksana Kode ("Tangan").

- Tugas: Mengeksekusi semua kode Python yang ditulis oleh agen lain dan melaporkan hasilnya.

2. AssistantAgent (sudoku_generator)

- Peran: Pembuat Puzzle.

- Tugas: Menulis kode Python untuk membuat grid puzzle 9x9.

3. AssistantAgent (sudoku_solver)

- Peran: Pemecah Masalah.

- Tugas: Menulis kode Python untuk menemukan solusi dari puzzle yang diberikan.

4. AssistantAgent (sudoku_verifier)

- Peran: Penjamin Kualitas.

- Tugas: Menulis kode Python untuk memverifikasi apakah solusi 100% valid.

5. AssistantAgent (sudoku_visualization)

- Peran: Presenter.

- Tugas: Menulis kode Python untuk mencetak puzzle dan solusi dalam format ASCII yang mudah dibaca.

## Alur Kerja

Manajer Proyek mengarahkan tim dalam urutan yang ketat:
Minta -> Generate -> Solve -> Verify -> Visualize -> Selesai.

## Konfigurasi Model

Proyek ini dapat menggunakan model LLM apa pun yang kompatibel dengan API OpenAI (misalnya DeepSeek, Groq, dll.).

1. File .env

Buat file .env untuk menyimpan kunci API Anda. File ini harus tetap rahasia.

Contoh untuk DeepSeek:

## Kunci API dari DeepSeek

DS_KEY="your-deepseek-api-key-goes-here"

## URL dasar resmi DeepSeek

BASE_URL="[https://models.github.ai/inference](https://models.github.ai/inference)""

## Contoh untuk OpenAI:

OPENAI_KEY="your-openai-api-key-goes-here"

2. Objek llm_config (dalam Python)

Objek ini membaca variabel .env Anda untuk menghubungkan AutoGen ke model.

llm_config = {
"config_list": [
{
"model": "deepseek-r1-0528",
"api_key": os.environ.get("DS_KEY"),
"base_url": os.environ.get("BASE_URL"),
}
],
"cache_seed": 42, # Mengaktifkan cache untuk respons yang konsisten
"temperature": 0, # Menghilangkan keacakan
}

## Cara Menjalankan

1. Clone Repositori:

   git clone [https://github.com/your-username/sudokuMultiAgen.git](https://github.com/your-username/sudokuMultiAgen.git)
   cd sudokuMultiAgen

2. Buat & Aktifkan Virtual Environment:

# (Gunakan python3 -m venv envm di macOS/Linux)

python -m venv envm

# (Gunakan source envm/bin/activate di macOS/Linux)

.\envm\Scripts\activate

3. Instal Dependensi:

pip install -r requirements.txt

4. Buat File .env Anda:

   - Buat file bernama .env dan tambahkan kunci API Anda (lihat bagian "Konfigurasi").

5. Buat Direktori Kerja:
   Agen perlu "sandbox" untuk menyimpan dan menjalankan kode.

mkdir sudoku_game

6. Jalankan Proyek!

python your_main_script_name.py
