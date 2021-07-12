Deskripsi:
Program ini digunakan untuk mengecek harga saham hari ini dan kemarin, mencari presentase perubahan harganya.
Kemudian program mencari berita terkait saham yang sedang dibahas, untuk selanjutnya mengirimkannya melalui sms.

API yang digunakan:
* https://www.alphavantage.co/  # untuk mengetahui harga saham
* https://newsapi.org/          # untuk mencari berita
* https://newsapi.org/          # untuk mengirim sms

Module yang digunakan:
* os module         # untuk mengakses environment variables
* datetime module   # untuk mengetahui tanggal hari ini
* requests module   # send http request
* twilio module     # untuk mengirim sms
