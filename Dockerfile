
# DOockerfile
# Python image (Docker Hub'dan indirilecek)
FROM python:3.9-slim-buster

# Çalışma dizini oluşturma
WORKDIR /app

# Gerekli dosyaları kopyalama
COPY . /app

# Gerekli paketleri yükleme
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Uygulamayı başlatma
CMD ["python", "app.py"]
