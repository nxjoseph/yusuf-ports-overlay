--- src/download/videos.py.orig	2025-02-04 16:49:29 UTC
+++ src/download/videos.py
@@ -312,8 +312,8 @@ def on_video_clicked(button, self, entry):
         else:
             # Show error dialog if something went wrong
             error_body = (
-                f"{_("An error occurred:")}\n\n"
-                f"{_("The video platform may not be supported or you may be being blocked by the platform. If you have an active VPN connection that might be the cause, or you can try importing your browser's cookies through a cookies.txt file.")}\n\n\n"
+                f'{_("An error occurred:")}\n\n'
+                f'{_("The video platform may not be supported or you may be being blocked by the platform. If you have an active VPN connection that might be the cause, or you can try importing your browsers cookies through a cookies.txt file.")}\n\n\n'
                 "────────────────────────────\n\n\n"
                 f"{self.escape_special_characters(ytdlp_error)}"
             )
@@ -370,4 +370,4 @@ def on_video_option_download_clicked(self, prefswindow
         else:
             break
 
-    on_download_clicked(None, self, url, filename, None, "video", video_options, False, self.appconf["download_directory"])
\ No newline at end of file
+    on_download_clicked(None, self, url, filename, None, "video", video_options, False, self.appconf["download_directory"])
