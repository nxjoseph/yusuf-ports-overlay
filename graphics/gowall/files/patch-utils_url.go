--- utils/url.go.orig	2024-11-16 16:44:51 UTC
+++ utils/url.go
@@ -19,6 +19,8 @@ func OpenURL(url string) error {
 		cmd = exec.Command("open", url)
 	case "linux":
 		cmd = exec.Command("xdg-open", url)
+	case "freebsd":
+		cmd = exec.Command("xdg-open", url)
 
 	default:
 		return fmt.Errorf("unsupported platform")
