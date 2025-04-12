FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the server
# CMD ["gunicorn", "filehub.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["gunicorn", "filemanager.wsgi:application", "--bind", "0.0.0.0:8000"]

