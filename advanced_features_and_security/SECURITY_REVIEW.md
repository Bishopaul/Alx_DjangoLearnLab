# Security Review

## HTTPS and Transport Security

- `SECURE_SSL_REDIRECT = True` forces all HTTP requests to be redirected to HTTPS.
- HSTS is enabled with:
  - `SECURE_HSTS_SECONDS = 31536000`
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - `SECURE_HSTS_PRELOAD = True`
  This ensures browsers only access the site over HTTPS for one year and allows inclusion in preload lists.

## Secure Cookies

- `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True` ensure cookies are only sent over HTTPS, protecting them from interception.

## Secure Headers

- `X_FRAME_OPTIONS = "DENY"` protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` enables browser XSS protection.

## Potential Improvements

- Use a CDN with HTTPS enforced.
- Add CSP (Content Security Policy) for further XSS mitigation.
- Regularly rotate TLS certificates and enforce strong cipher suites at the web server level.
