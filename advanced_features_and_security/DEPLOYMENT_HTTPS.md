# HTTPS Deployment Configuration

## SSL/TLS Setup

In production, the Django application is served behind a web server such as Nginx or Apache.

### Example (Nginx)

- Obtain an SSL/TLS certificate (e.g., via Let's Encrypt).
- Configure Nginx to:
  - Listen on port 443 with the SSL certificate and key.
  - Proxy pass HTTPS traffic to the Django application (gunicorn/uwsgi).
  - Redirect all HTTP (port 80) traffic to HTTPS.

Example snippet:

server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
