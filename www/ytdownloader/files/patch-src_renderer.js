--- src/renderer.js.orig	2024-05-28 19:42:41 UTC
+++ src/renderer.js
@@ -4,7 +4,7 @@ if (os.platform() === "win32") {
 if (os.platform() === "win32") {
	ffmpeg = `"${__dirname}\\..\\ffmpeg.exe"`;
 } else {
-	ffmpeg = `"${__dirname}/../ffmpeg"`;
+	ffmpeg = cp.execSync("which ffmpeg").toString("utf8").split("\n")[0].trim();
 }

 const fs = require("fs");
