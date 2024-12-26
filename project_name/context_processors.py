from django.conf import settings


def vendor_files(request):
	static_dir = settings.CORE_DIR / "static"
	vendor_dir = static_dir / "vendor"
	js_files = [x.relative_to(static_dir) for x in vendor_dir.glob("**/*.js")]
	css_files = [x.relative_to(static_dir) for x in vendor_dir.glob("**/*.css")]

	return {
		"vendor_js": js_files,
		"vendor_css": css_files,
	}

from core.misc.field_choices import (
	Genders,
) 
def form_values(request):
	return {
		"genders": Genders.choices
	}

def brand(request):
	return settings.BRAND
