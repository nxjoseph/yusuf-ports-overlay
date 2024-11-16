--- internal/image/image.go.orig	2024-11-16 16:45:41 UTC
+++ internal/image/image.go
@@ -162,6 +162,8 @@ func OpenImage(filePath string) error {
 		cmd = exec.Command("open", filePath)
 	case "linux":
 		cmd = exec.Command("xdg-open", filePath)
+	case "freebsd":
+		cmd = exec.Command("xdg-open", filePath)
 
 	default:
 		return fmt.Errorf("unsupported platform")
