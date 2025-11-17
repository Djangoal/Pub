[app]

title = QuickAdApp
package.name = quickadapp
package.domain = org.example
source.dir = app
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3, kivy==2.2.1, android, jnius, https://github.com/MichaelStott/KivMob/archive/refs/heads/master.zip

orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21

# Permissions nécessaires pour AdMob
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Metadata AdMob (App ID de test Google)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713

# Firebase Ads
android.gradle_dependencies = com.google.firebase:firebase-ads:21.4.0

# AndroidX
android.enable_androidx = True

# Empêche les conflits de compression
android.allow_backup = False

# Accept all SDK licenses automatically
android.accept_sdk_license = True

# Support multi-architecture si besoin (facultatif)
# android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
