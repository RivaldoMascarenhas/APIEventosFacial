from .auth import router_auth
from .users import router_users

# Routers
all_routers = [
    router_auth,
    router_users,
]

__all__ = ["all_routers"]