# requirements: ajoute KivMob via l'URL GitHub (ou installe via pip local)
requirements = python3, kivy, android, jnius, https://github.com/MichaelStott/KivMob/archive/refs/heads/master.zip

# permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# versions (exemples recommandés)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

# dépendance gradle pour les ads (Google Mobile Ads / Firebase Ads)
android.gradle_dependencies = com.google.firebase:firebase-ads:21.4.0
android.enable_androidx = True

# metadata: App ID (Test App ID Google). Remplace par le tien pour la production.
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3940256099942544~3347511713
