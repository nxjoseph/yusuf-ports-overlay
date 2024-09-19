--- src/droidcam.c.orig	2024-09-19 13:28:33.408823000 +0300
+++ src/droidcam.c	2024-09-19 13:28:42.000649000 +0300
@@ -50,7 +50,7 @@
 extern const char *thread_cmd_val_str;
 extern char snd_device[32];
 extern char v4l2_device[32];
-const char *APP_ICON_FILE = "/opt/droidcam-icon.png";
+const char *APP_ICON_FILE = "/usr/local/share/pixmaps/droidcam-icon.png";
 
 void * AudioThreadProc(void * args);
 void * VideoThreadProc(void * args);
