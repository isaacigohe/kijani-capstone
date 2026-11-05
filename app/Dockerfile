FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN useradd -m kijani && chown -R kijani:kijani /app
USER kijani
EXPOSE 8080
CMD ["python", "app.py"]
