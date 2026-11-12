[app]

# (str) Title of your application
title = Game Subtitle Overlay

# (str) Package name
package.name = gamesubtitle

# (str) Package domain (needed for android packaging)
package.domain = org.overlay

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
# تأكد من تضمين مكتبات بايثون ومعالجة النصوص العربية
requirements = python3,kivy,arabic-reshaper,python-bidi,setuptools

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) The permissions to grant to your application
# إضافة صلاحية عرض الشاشة فوق التطبيقات الأخرى (System Alert Window)
android.permissions = SYSTEM_ALERT_WINDOW

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
