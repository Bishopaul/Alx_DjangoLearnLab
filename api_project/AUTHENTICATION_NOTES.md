# Authentication & Permissions

- Token authentication enabled via `rest_framework.authtoken`.
- Tokens generated using DRF’s built-in `obtain_auth_token` view.
- Default permission class: `IsAuthenticated`.
- BookViewSet requires authentication for all CRUD operations.
- Token must be included in the Authorization header for all requests.
