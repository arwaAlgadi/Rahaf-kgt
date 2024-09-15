import tkinter as tkfrom tkinter import messagebox
import pyperclip
# دالة التشفير باستخدام قيصر المعدلةdef encrypt_caesar(plain_text, shift):
    all_chars = 'abcdefghijklmnopqrstuvwxyz'  # الأبجدية    cipher_text = ''
    for letter in plain_text:        if letter == ' ':  # احتفظ بالمسافات
            cipher_text += ' '        elif letter.lower() in all_chars:
            # حساب الموقع الجديد للحرف            index = (all_chars.index(letter.lower()) + shift) % len(all_chars)
            new_letter = all_chars[index]
            # الحفاظ على الأحرف الكبيرة والصغيرة            if letter.isupper():
                cipher_text += new_letter.upper()            else:
                cipher_text += new_letter        else:
            cipher_text += letter  # للحروف الخاصة والأرقام    return cipher_text
# دالة فك التشفير باستخدام نفس دالة التشفير مع shift سالب
def caesar_decrypt(text, shift):    return encrypt_caesar(text, -shift)

# دالة نسخ النص إلى الحافظةdef copy_to_clipboard(text):
    pyperclip.copy(text)    messagebox.showinfo("نسخ", "تم نسخ النص إلى الحافظة")
# دالة التشفير
def encrypt_message():    message = message_entry.get()
    shift = int(shift_entry.get())  # قيمة شيفت مأخوذة من المستخدم    encrypted_message = encrypt_caesar(message, shift)
    encrypted_label.config(text=encrypted_message)
# دالة فك التشفيرdef decrypt_message():
    message = decrypt_entry.get()    shift = int(shift_entry.get())  # نفس قيمة الشيفت المستخدمة للتشفير
    decrypted_message = caesar_decrypt(message, shift)    decrypted_label.config(text=decrypted_message)
# إعداد النافذة الرئيسية
root = tk.Tk()root.title("تطبيق التشفير")
# تصميم واجهة جذابة
root.geometry("400x400")root.config(bg="#f0f8ff")
# حقل إدخال النص المراد تشفيره
message_label = tk.Label(root, text="أدخل النص للتشفير:", bg="#f0f8ff")message_label.pack(pady=10)
message_entry = tk.Entry(root, width=50)message_entry.pack(pady=5)
# حقل إدخال قيمة الشيفت
shift_label = tk.Label(root, text="أدخل قيمة الشيفت:", bg="#f0f8ff")
shift_label.pack(pady=10)shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)
# زر تشفير النصencrypt_button = tk.Button(root, text="تشفير", command=encrypt_message, bg="#4682b4", fg="white")
encrypt_button.pack(pady=10)
# عرض النص المشفرencrypted_label = tk.Label(root, text="", bg="#f0f8ff", wraplength=350)
encrypted_label.pack(pady=5)
# زر لنسخ النص المشفرcopy_encrypt_button = tk.Button(root, text="نسخ النص المشفر", command=lambda: copy_to_clipboard(encrypted_label.cget("text")), bg="#4682b4", fg="white")
copy_encrypt_button.pack(pady=5)
# حقل إدخال النص المراد فك تشفيرهdecrypt_label = tk.Label(root, text="أدخل النص لفك التشفير:", bg="#f0f8ff")
decrypt_label.pack(pady=10)decrypt_entry = tk.Entry(root, width=50)
decrypt_entry.pack(pady=5)
# زر فك التشفيرdecrypt_button = tk.Button(root, text="فك التشفير", command=decrypt_message, bg="#4682b4", fg="white")
decrypt_button.pack(pady=10)
# عرض النص المفكوكdecrypted_label = tk.Label(root, text="", bg="#f0f8ff", wraplength=350)
decrypted_label.pack(pady=5)
# زر لنسخ النص المفكوكcopy_decrypt_button = tk.Button(root, text="نسخ النص المفكوك", command=lambda: copy_to_clipboard(decrypted_label.cget("text")), bg="#4682b4", fg="white")
copy_decrypt_button.pack(pady=5)
# تشغيل النافذةroot.mainloop()