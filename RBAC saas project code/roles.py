roles_permissions = {
    "admin": ["view_dashboard", "edit_content", "delete_content"],
    "editor": ["view_dashboard", "edit_content"],
    "viewer": ["view_dashboard"]
}

# Function to check if a user has permission for a specific action
def has_permission(role, permission):
    return permission in roles_permissions.get(role, [])