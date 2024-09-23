--- mov_cli/dev_cli/preview.py.orig	2024-09-23 11:48:13 UTC
+++ mov_cli/dev_cli/preview.py
@@ -29,8 +29,8 @@ def image(id: str):
 def image(id: str):
     platform = what_platform()
 
-    if not platform == "Linux" and not platform == "Android":
-        print("Image preview only works on Linux & Android atm.")
+    if not platform == "Linux" and not platform == "FreeBSD" and not platform == "Android":
+        print("Image preview only works on Linux, FreeBSD & Android atm.")
         return False
 
     cache = Cache(
@@ -102,4 +102,4 @@ def slugify(value): # https://github.com/django/django
     )
 
     value = re.sub(r"[^\w\s-]", "", value.lower())
-    return re.sub(r"[-\s]+", "-", value).strip("-_")
\ No newline at end of file
+    return re.sub(r"[-\s]+", "-", value).strip("-_")
