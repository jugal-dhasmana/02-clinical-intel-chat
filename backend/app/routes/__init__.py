from .health import router as health_router
from .normalize import router as normalize_router
from .clinical_intel import router as clinical_intel_router

__all__ = ['health_router', 'normalize_router', 'clinical_intel_router']
