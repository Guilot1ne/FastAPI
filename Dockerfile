# Χρησιμοποιούμε το επίσημο Python image
FROM python:3.11

# Ορίζουμε το working directory
WORKDIR /app

# Αντιγράφουμε τα dependencies
COPY requirements.txt requirements.txt

# Εγκατάσταση των απαιτούμενων πακέτων
RUN pip install --no-cache-dir -r requirements.txt

# Αντιγράφουμε τα αρχεία της εφαρμογής
COPY . .  

# ✨ Εδώ προσθέτουμε το .env ✨
COPY .env .env

# Ορίζουμε την πόρτα που θα εκτελείται η εφαρμογή
EXPOSE 8000

# Εκκίνηση της εφαρμογής FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
