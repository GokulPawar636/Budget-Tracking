# 1️⃣ Base image
FROM python:3.12.7

# 2️⃣ Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Set work directory
WORKDIR /app

# 4️⃣ Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5️⃣ Copy project files
COPY . .

# 6️⃣ Expose Django port
EXPOSE 8000

# 7️⃣ Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
