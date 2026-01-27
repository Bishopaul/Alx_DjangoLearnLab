# Alx_DjangoLearnLab
Hands-on lab documentation and configurations for ALX Django module.

# Django Permissions & Groups — Access Control System

This module demonstrates how to implement custom permissions and group-based access control in Django.

---

## 1. Custom Permissions

The `Article` model defines four custom permissions:

- can_view
- can_create
- can_edit
- can_delete

These permissions appear automatically in Django Admin.

---

## 2. Groups Setup

Create the following groups in Django Admin:

### Viewers
- can_view

### Editors
- can_view
- can_create
- can_edit

### Admins
- can_view
- can_create
- can_edit
- can_delete

Assign users to these groups to control access.

---

## 3. Permission Enforcement in Views

Views use Django’s `@permission_required` decorator:

```python
@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
