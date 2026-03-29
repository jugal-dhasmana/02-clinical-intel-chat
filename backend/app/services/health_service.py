from app.core.settings import get_settings
from app.schemas.health import HealthResponse


class HealthService:
    def get_health(self) -> HealthResponse:
        settings = get_settings()
        return HealthResponse(status='ok', app='clinical-intel-chat', version=settings.app_version)
