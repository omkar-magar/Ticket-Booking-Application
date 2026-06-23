[app]

# (str) Title of your application
title = AMG

# (str) Package name
package.name = amg

# (str) Package domain (needed for android/ios packaging)
package.domain = com.alohatechnology

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, .venv, .venv-1, .git, __pycache__

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# Pinned to the versions verified on the dev machine.
requirements = python3,kivy==2.3.1,kivymd==1.2.0,pillow,qrcode

# (str) Presplash of the application
presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Presplash background color (white) so the native Android splash matches
# the in-app SplashScreen for a seamless hand-off.
android.presplash_color = #FFFFFF

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/app_icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (str) The format used to package the app for release mode (aab or apk or aar).
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (bool) Skip Buildozer's automatic SDK package install/update. The CI workflow
# pre-installs platform-tools, platforms;android-34 and build-tools 33.0.2 (the
# last build-tools that still ships `aidl`, which 34+ removed). Skipping the
# update stops Buildozer from installing the latest build-tools and re-breaking
# the aidl check.
android.skip_update = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
