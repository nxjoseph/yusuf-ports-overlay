--- src/download/thread.py.orig	2025-02-04 16:32:56 UTC
+++ src/download/thread.py
@@ -215,7 +215,7 @@ class DownloadThread(threading.Thread):
                     self.video_stop_event.clear()
                     self.cancelled = True
                 except Exception as e:
-                    GLib.idle_add(self.speed_label.set_text, f"{_("An error occurred:")} {self.app.escape_special_characters(str(e))}")
+                    GLib.idle_add(self.speed_label.set_text, f'{_("An error occurred:")} {self.app.escape_special_characters(str(e))}')
                     self.video_stop_event.clear()
                     self.cancelled = True
                     GLib.idle_add(self.set_failed, None)
@@ -603,4 +603,4 @@ class DownloadThread(threading.Thread):
 
         self.stop(False)
         GLib.idle_add(self.pause_button.set_visible, False)
-        self.app.filter_download_list("no", self.app.applied_filter)
\ No newline at end of file
+        self.app.filter_download_list("no", self.app.applied_filter)
